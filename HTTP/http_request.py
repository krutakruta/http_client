import copy


class HTTPRequest:
    def __init__(self):
        self.starting_line = ""
        self.headers = {}
        self.message_body = ""

    def request_to_bytes(self):
        return "{}\n{}\n\n{}".format(
            self._starting_line,
            "\n".join("{}: {}".format(key, val)
                      for key, val in self.headers.items()),
            self._message_body).encode()
