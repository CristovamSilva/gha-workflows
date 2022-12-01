from fastapi import APIRouter
from http import HTTPStatus
from ..controllers.crud import create, read, update, delete

router = APIRouter(prefix="/database")


@router.post("/create", status_code=HTTPStatus.CREATED)
async def register(collection, object):
    await create(collection, object)
    return {"message": "created"}


@router.get("/read", status_code=HTTPStatus.OK)
async def fetch(collection, filter):
    object = await read(collection, filter)
    return {"message": object}


@router.post("/update", status_code=HTTPStatus.OK)
async def change(collection, filter, object):
    await update(collection, filter, object)
    return {"message": "updated"}


@router.post("/delete", status_code=HTTPStatus.NO_CONTENT)
async def remove(collection, filter):
    await delete(collection, filter)
    return {"message": "deleted"}
