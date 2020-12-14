"""
Here you should do all needed actions. Standart configuration of docker container
will run your application with this file.
"""
import uvicorn
from fastapi import FastAPI
from loguru import logger

from server.config import openapi_config
from dbs import mongo_motor_client
from server.initializer import init


app = FastAPI(
    title=openapi_config.name,
    version=openapi_config.version,
    description=openapi_config.description,
)


@app.on_event('startup')
async def startup():
    await mongo_motor_client.start_session()


@app.on_event('shutdown')
async def shutdown():
    await mongo_motor_client.end_session()


logger.info('Starting application initialization...')
init(app)
logger.success('Successfully initialized!')


if __name__ == '__main__':
    uvicorn.run('server.app:app', host='0.0.0.0', port=8000, reload=True)