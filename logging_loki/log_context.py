import json


class LogContext:
    def __init__(self):
        self._message = ""

    def set_message(self, message):
        self._message = message

    def to_string(self):
        return json.dumps({
            "message": self._message
        })

    def get_tags(self):
        return dict()
