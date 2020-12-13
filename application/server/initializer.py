from inspect import getmembers

from fastapi import FastAPI
from server.server.utils.api import TypedAPIRouter


def init(app: FastAPI):
    """
    Init routers and etc.
    :return:
    """
    init_routers(app)
    init_db(app)


def init_db(app: FastAPI):
    """
    Init database models.
    :param app:
    :return:
    """


def init_routers(app: FastAPI):
    """
    Initialize routers defined in `app.api`
    :param app:
    :return:
    """
    from web import routers

    routers = [o[1] for o in getmembers(routers) if isinstance(o[1], TypedAPIRouter)]

    for router in routers:
        app.include_router(**router.dict())
