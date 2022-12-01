from fastapi import FastAPI
from . import dependencies
from . import routes


def create_app() -> FastAPI:
    app = FastAPI()

    dependencies.init()
    routes.init(app)

    return app
