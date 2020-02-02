import copy
import re
from enum import Enum


class HTTPResponse:
    def __init__(self):
        self._starting_line = {}
        self.headers = {}
        self.message_body = ""
        self.status = None
        self.content_type = None

    def set_starting_line(self, line):
        parts = re.search(r"HTTP/(.*?) (\d{3})", line)
        self._starting_line["http_version"] = parts.group(1)
        self._starting_line["status_code"] = parts.group(2)

    @property
    def starting_line(self):
        return self._starting_line


class HTTPStatus(Enum):
    Informational = 1
    Success = 2
    Redirection = 3
    Client_error = 4
    Server_error = 5

