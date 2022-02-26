import logging
from fastapi import FastAPI

from projekt_prog.api.routers.mian_router import main_router

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(main_router)