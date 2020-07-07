class ApiResponse(object):
    def __init__(self, status="success", data=None, message=None):
        self.status = status
        self.data = data
        self.message = message

    def to_dict(self):
        if self.message is not None and self.data is not None:
            return {
                "status": self.status,
                "data": self.data,
                "message": self.message
            }
        if self.message is not None:
            return {
                "status": self.status,
                "message": self.message
            }
        if self.data is not None:
            return {
                "status": self.status,
                "data": self.data
            }
        return {
            "status": self.status
        }
