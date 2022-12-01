from ..dependencies import db


async def create(collection, object):
    db.create(collection, object)


async def read(collection, filter):
    db.read(collection, filter)


async def update(collection, filter, object):
    db.update(collection, filter, object)


async def delete(collection, filter):
    db.delete(collection, filter)
