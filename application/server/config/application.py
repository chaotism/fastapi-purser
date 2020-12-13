"""Config of apps"""
from pydantic import Field

from server.config.base import BaseSettings


class ApplicationSettings(BaseSettings):  # TODO: not used fields
    """Application env values"""

    is_test: bool = Field(True, env="API_TEST")
    is_debug: bool = Field(True, env="API_DEBUG")

    host: str = Field("0.0.0.0", env="API_HOST")
    port: int = Field(8000, env="API_PORT")
