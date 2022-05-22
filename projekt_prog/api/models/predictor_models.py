from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Decision(Enum):
    SELL = 'SELL'
    BUY = 'BUY'


class DecisionModel(BaseModel):
    decision: Decision


class BuySellModel(BaseModel):
    buy: datetime
    sell: datetime
    profit: str
