from client_modules.http_client import HTTPClient


class ArgsParser:
    def __init__(self):
        self._http_request = HTTPClient()

    def parse(self, args):
        self._check_args(args)


    def _check_args(self, args):
        if type(args) is not list:
            raise TypeError(
                "Command line args should be {} but it is {}".format(
                    type(list), type(args)))

    def reset_parser(self):
        pass
