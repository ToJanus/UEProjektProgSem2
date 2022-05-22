import logging
import os
from datetime import datetime
from typing import Any

from fastapi import APIRouter

import projekt_prog
from projekt_prog.api.models.main_models import ServerInfoModel

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))

main_router = APIRouter()


@main_router.get('/server_info', tags=['server info'], response_model=ServerInfoModel)
async def get_server_info():
    dt_now = datetime.now().astimezone().replace(microsecond=0)

    return {
        'version': projekt_prog.__version__,
        'server_datetime': dt_now,
        'server_timezone': str(dt_now.tzinfo)
    }