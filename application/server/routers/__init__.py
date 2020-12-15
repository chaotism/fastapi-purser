from server.utils.api import TypedAPIRouter as APIRouter

from .api.endpoints import api_router
from .health.endpoints import health_router


base_router = APIRouter()

base_router.include_router(api_router, tags=['api'])
base_router.include_router(health_router, tags=['health'])
