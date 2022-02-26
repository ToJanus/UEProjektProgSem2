import logging
import os

import uvicorn as uvicorn
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
logger.setLevel(LOG_LEVEL)

if __name__ == '__main__':
    logger.info("Starting server")

    uvicorn.run('projekt_prog.api.api:app',
                host=os.environ.get('HOST', '0.0.0.0'),
                port=int(os.environ.get('PORT', '5050')),
                log_level=LOG_LEVEL.lower())
