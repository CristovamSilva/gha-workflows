from databases import MemoryDB as database

db = database.init_database("crudDb")


def init():
    return True
