class InvalidUsage(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def to_dict(self):
        return {
            'message': message,
        }