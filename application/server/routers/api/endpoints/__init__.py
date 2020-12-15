from server.utils.api import TypedAPIRouter as APIRouter
from .accounts import account_router
from .transactions import transaction_router
from .users import user_router


api_router = APIRouter(prefix='/api')

api_router.include_router(account_router, prefix='/accounts',  tags=['accounts'])
api_router.include_router(transaction_router, prefix='/transactions', tags=['transactions'])
api_router.include_router(user_router, prefix='/users', tags=['users'])
