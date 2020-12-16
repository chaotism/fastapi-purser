"""Config of DBS"""
from pydantic import Field

from .base import BaseSettings
from .application import ApplicationSettings

MONGO_DEFAULT_DB_URI = 'mongodb://localhost:27017'
MONGO_DEFAULT_DB_NAME = 'purser'
MONGO_DEFAULT_DB_TEST_NAME = 'test'


class MongodbSettings(BaseSettings):
    """Mongodb env values"""
    uri: str = Field(MONGO_DEFAULT_DB_URI,  env='MONGO_URI')
    db: str = Field(MONGO_DEFAULT_DB_NAME,  env='MONGO_DB')

    @classmethod
    def generate(cls):
        """Generate MongoDD settings (with sqlite if tests)"""
        application_settting = ApplicationSettings()
        if application_settting.is_test:
            return MongodbSettings(db=MONGO_DEFAULT_DB_TEST_NAME)
        return MongodbSettings()
