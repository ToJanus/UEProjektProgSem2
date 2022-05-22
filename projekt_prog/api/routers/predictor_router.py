import logging
import os
from datetime import datetime, timedelta
from io import BytesIO

import numpy as np
import pandas as pd

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from predict import prepare_data, get_X_and_y, get_X_predict, get_fitted_model, get_predict

from projekt_prog.api.models.predictor_models import DecisionModel, BuySellModel

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))

predictor_router = APIRouter()


async def get_csv(file: UploadFile = File(...)) -> pd.DataFrame:
    try:
        contents = await file.read()
        buffer = BytesIO(contents)
        data = pd.read_csv(buffer)
        buffer.close()
    except:
        raise HTTPException(status_code=422, detail="Bad file format")

    logger.debug(f"File uploaded")
    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)
    return data


def get_prediction(data: pd.DataFrame) -> np.array:
    prediction_days = 30
    df = prepare_data(data, prediction_days)
    X, y = get_X_and_y(df, prediction_days)
    X_predict = get_X_predict(df, prediction_days)
    model = get_fitted_model(X, y)
    return get_predict(X_predict, model)


@predictor_router.post('/buy_sell_predict', tags=['Buy/Sell prediction'], response_model=BuySellModel)
async def buy_sell_predict(data: pd.DataFrame = Depends(get_csv)):
    last_date = data['Date'].iloc[-1]

    predict = get_prediction(data)

    min_index = int(np.argmin(predict))
    max_index = int(np.argmax(predict[min_index:]) + min_index)

    return {
        'buy': last_date + timedelta(days=min_index+1),
        'sell': last_date + timedelta(days=max_index + 1),
        'profit': f'{round(predict[min_index] / predict[max_index] * 100)} %'
    }


@predictor_router.post('/decision_predict', tags=['decision prediction'], response_model=DecisionModel)
async def decision_predict(data: pd.DataFrame = Depends(get_csv)):
    last_value = data.iloc[-1]['Close']

    predict = get_prediction(data)

    avg = np.mean(predict)

    return {
        'decision': 'BUY' if last_value < avg else 'SELL'
    }
