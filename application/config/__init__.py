"""Config of application"""
from .application import ApplicationSettings
from .db import MongodbSettings
from .openapi import OpenAPISettings

application_config = ApplicationSettings()
mongodb_config = MongodbSettings.generate()
openapi_config = OpenAPISettings.generate()
