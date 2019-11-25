from HTTP.PartsOfRequest.starting_line import StartingLine


class HTTPRequest:
    def __init__(self):
        self._starting_line = None
        self._request_header_fields = None
        self._message_body = None

    def set_starting_line(self, start_line):
        if start_line is not StartingLine:
            raise TypeError("{} isn't {} type".format(
                type(start_line), type(StartingLine)))
        self._starting_line = start_line
