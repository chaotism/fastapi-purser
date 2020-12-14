from fastapi import APIRouter

from server.routers.api.endpoints import transaction, users

api_router = APIRouter(prefix='/api')


api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(transaction.router, prefix='/items', tags=['items'])
