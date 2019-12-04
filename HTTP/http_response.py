import copy
import re


class HTTPResponse:
    def __init__(self):
        self._starting_line = {}
        self._headers = {}
        self._message_body = ""

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

    def is_it_1xx_response(self):
        return self._is_it_x_response("1")

    def is_it_2xx_response(self):
        return self._is_it_x_response("2")

    def is_it_3xx_response(self):
        return self._is_it_x_response("3")

    def is_it_4xx_response(self):
        return self._is_it_x_response("4")

    def is_it_5xx_response(self):
        return self._is_it_x_response("5")

    def _is_it_x_response(self, x):
        return ("status_code" in self._starting_line and
                self._starting_line["status_code"][0] == x)

    @property
    def starting_line(self):
        return self._starting_line

    @property
    def headers(self):
        return self._headers

    @property
    def message_body(self):
        return self._message_body
