import logging
from fastapi import FastAPI

from projekt_prog.api.routers.mian_router import main_router
from projekt_prog.api.routers.predictor_router import predictor_router

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(main_router)
app.include_router(predictor_router)
