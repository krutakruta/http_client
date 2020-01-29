import copy


class HTTPRequest:
    def __init__(self):
        self._starting_line = None
        self._headers = {}
        self._message_body = None

    def set_starting_line(self, line):
        self._starting_line = line

    def add_header(self, header, options):
        if isinstance(options, list):
            self._headers[header] = "" if options == [] else "; ".join(options)
        elif isinstance(options, str):
            self._headers[header] = options

    def add_header_option(self, header, option):
        self._headers[header].append(option)

    def set_message_body(self, message_body):
        self._message_body = message_body

    def request_to_bytes(self):
        return "{}\n{}\n\n{}".format(
            self._starting_line,
            "\n".join("{}: {}".format(key, val)
                      for key, val in self.headers.items()),
            self._message_body).encode()

    @property
    def starting_line(self):
        return self._starting_line

    @property
    def headers(self):
        return copy.copy(self._headers)

    @property
    def message_body(self):
        return self._message_body
