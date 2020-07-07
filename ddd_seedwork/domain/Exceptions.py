class DomainNotification(object):

    def __init__(self, key: str, error: str):
        self.key = key
        self.error = error

    def to_dict(self):
        return {
            "key": self.key,
            "error": self.error
        }


class DomainError(Exception):
    def __init__(self, notifications, message):
        super().__init__(message)
        self.notifications = notifications
