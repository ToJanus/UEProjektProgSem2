from datetime import datetime
from pydantic import BaseModel


class ServerInfoModel(BaseModel):
    version: str
    server_datetime: datetime
    server_timezone: str

