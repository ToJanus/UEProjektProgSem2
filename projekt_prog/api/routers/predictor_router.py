import logging
import os
from io import BytesIO
import pandas as pd
from typing import Any

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import ValidationError

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))

predictor_router = APIRouter()


@predictor_router.post('/server_info', tags=['Upload data'])
async def upload_data(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        buffer = BytesIO(contents)
        df = pd.read_csv(buffer)
        buffer.close()
    except:
        raise HTTPException(status_code=422, detail="Bad file format")

    logger.debug(f"File uploaded")

    return df.to_dict(orient='records')
