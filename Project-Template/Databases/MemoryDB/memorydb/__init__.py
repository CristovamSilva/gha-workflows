from uuid import uuid4


class MemoryDB:
    def __init__(self) -> None:
        self.db = dict()

    def create(self, object):
        id = str(uuid4())
        self.db[id] = object
        print(self.db)
        return {"id": id}

    def read(self, filter):
        return self.db[filter]

    def update(self, filter, object):
        self.db[filter] = object
        return True

    def delete(self, filter):
        del self.db[filter]
        return True


def init_database():
    db = MemoryDB()
    return db
