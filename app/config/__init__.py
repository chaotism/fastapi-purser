"""Config of application"""
from .db import TortoiseSettings
from .openapi import OpenAPISettings

application_config = OpenAPISettings.generate()
tortoise_config = TortoiseSettings.generate()
openapi_config = OpenAPISettings.generate()
