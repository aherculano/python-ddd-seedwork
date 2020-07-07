class PersistenceError(Exception):
    pass


class NotFoundError(PersistenceError):
    pass


class DuplicateError(PersistenceError):
    pass
