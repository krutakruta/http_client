import copy


class HTTPRequest:
    def __init__(self):
        self._starting_line = ""
        self._headers = {}
        self._message_body = ""

    def set_starting_line(self, line):
        self._starting_line = line

    def add_header(self, header, option):
        self._headers[header] = option

    def set_message_body(self, message_body):
        self._message_body = message_body

    def create_request_text(self):
        return "{}\n{}\n\n{}".format(
            self._starting_line,
            "\n".join("{}: {}".format(key, val)
                      for key, val in self.headers.items()),
            self._message_body)

    @property
    def starting_line(self):
        return self._starting_line

    @property
    def headers(self):
        return copy.copy(self._headers)

    @property
    def message_body(self):
        return self._message_body
