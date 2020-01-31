import copy
import re
from enum import Enum


class HTTPResponse:
    def __init__(self):
        self._starting_line = {}
        self._headers = {}
        self._message_body = ""
        self._status = None

    def set_starting_line(self, line):
        parts = re.search(r"HTTP/(.*?) (\d{3})", line)
        self._starting_line["http_version"] = parts.group(1)
        self._starting_line["status_code"] = parts.group(2)

    def add_header(self, header, options):
        if isinstance(options, list):
            self._headers[header] = options
        elif isinstance(options, str):
            self._headers[header] = list(options.split("; "))

    def add_header_option(self, header, option):
        self._headers[header].append(option)

    def set_message_body(self, message_body):
        self._message_body = message_body

    @property
    def starting_line(self):
        return self._starting_line

    @property
    def headers(self):
        return self._headers

    @property
    def message_body(self):
        return self._message_body

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


class HTTPStatus(Enum):
    Informational = 1
    Success = 2
    Redirection = 3
    Client_error = 4
    Server_error = 5
