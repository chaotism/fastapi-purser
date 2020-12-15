from server.utils.api import TypedAPIRouter as APIRouter

from .app_info import app_info_router


health_router = APIRouter(prefix='/health')
health_router.include_router(app_info_router, prefix='/app_info', tags=['app_info'])
