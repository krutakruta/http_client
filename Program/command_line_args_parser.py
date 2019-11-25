from HTTP.HTTP_methods import HTTP_Methods
from UserModules.UserRequests.command_line_service_request import CommandLineServiceRequest
from UserModules.UserRequests.command_line_http_request import CommandLineHTTPRequest
from Errors.wrong_method_error import WrongMethodError
from Auxiliary.helper import Helper


# В соответствии с регламентом программы(команды, параметры, опции) парсит
# аргументы командной строки


class CommandLineArgsParser:
    def __init__(self):
        self._request = None

    def parse(self, args):
        type_of_user_request = self._identify_user_request(args)
        if type_of_user_request is CommandLineHTTPRequest:
            self._request = CommandLineHTTPRequest()
            #self._parse_command_line_http_request(args)
        else:
            self._request = CommandLineServiceRequest()
            self._parse_command_line_service_request(args)

    def _parse_command_line_service_request(self, args):
        pass

    def _identify_user_request(self, args):
        if (len(args) == 2 and
                not Helper.is_service_command(args[1]) or
                len(args) > 2 and Helper.is_http_method(args[1])):
            return CommandLineHTTPRequest
        else:
            return CommandLineServiceRequest

    def reset_parser(self):
        self._request = None
