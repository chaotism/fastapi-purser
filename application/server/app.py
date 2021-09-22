"""
Here you should do all needed actions. Standart configuration of docker container
will run your application with this file.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from loguru import logger

from config import openapi_config, application_config
from dbs import mongo_motor_client
from server.routers import base_router as routers


logger.info('Starting application initialization...')
app = FastAPI(
    title=openapi_config.name,
    version=openapi_config.version,
    description=openapi_config.description,
)


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse("/docs")

app.include_router(routers)

logger.success('Successfully initialized!')


@app.on_event('startup')
async def startup():
    await mongo_motor_client.start_session()


@app.on_event('shutdown')
async def shutdown():
    await mongo_motor_client.end_session()


if __name__ == '__main__':
    uvicorn.run('server.app:app', host=application_config.host, port=application_config.port, reload=True)
