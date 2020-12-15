from fastapi import APIRouter

from server.routers.api.endpoints import transactions, users

api_router = APIRouter(prefix='/api')


api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(transactions.router, prefix='/transactions', tags=['items'])
