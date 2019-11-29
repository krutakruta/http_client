from Source.Errors.wrong_method_argument_error import WrongMethodArgumentError
from Source.Errors.wrong_parameter_error import WrongParameterError
from Source.HTTP.http_methods_params import HTTPMethodsParams
from Source.UserRequests.command_line_service_request import CommandLineServiceRequest
from Source.UserRequests.command_line_http_request import CommandLineHTTPRequest
from Source.Service.service_commands import ServiceCommands
from Source.HTTP.http_methods import HTTPMethods
from urllib.parse import urlparse


# В соответствии с регламентом программы(команды, параметры, опции) парсит
# аргументы командной строки


class CommandLineArgsParser:
    def __init__(self):
        self._request = None

    def parse(self, args):
        type_of_user_request = self._identify_user_request(args)
        try:
            if type_of_user_request is CommandLineHTTPRequest:
                self._request = CommandLineHTTPRequest()
                self._parse_command_line_http_request(args)
            else:
                self._request = CommandLineServiceRequest()
                self._parse_command_line_service_request(args)
        except (WrongParameterError, WrongMethodArgumentError):
            return self._create_help_user_request()
        else:
            return self._request

    def _parse_command_line_service_request(self, args):
        if (len(args) == 1 or len(args) > 1 and (  # Если ничего не введено после python main.py
                args[1] == ServiceCommands.help_command() or
                not ServiceCommands.is_command(args[1]))):
            self._request.set_command(ServiceCommands.help_command())
            if len(args) >= 3:
                self._request.set_parameter(args[2])

    def _parse_command_line_http_request(self, args):   # устанавливаем http метод, его аргумент и параметры
        if HTTPMethods.is_method(args[1]):
            self._request.set_method(args[1])
            self._request.set_method_argument(args[2])
            method_arguments = args[3:]
        else:
            self._request.set_method(HTTPMethods.get_method())
            self._request.set_method_argument(args[1])
            method_arguments = args[2:]
        self._set_method_parameters(method_arguments)

    def _set_method_parameters(self, arguments):
        if not self._arguments_are_correct_sequence(arguments):
            raise WrongParameterError("Incorrect parameters sequence")
        for i in range(len(arguments)):
            if arguments[i].startswith("-"):
                self._request.add_method_parameter(arguments[i])
            elif i > 0 and arguments[i-1].startswith("-"):
                self._request.set_parameter_option(
                    arguments[i-1], arguments[i])

    def _arguments_are_correct_sequence(self, arguments):
        if len(arguments) == 1 and not arguments[0].startswith("-"):
            return False
        for i in range(1, len(arguments)):
            if not (arguments[i-1].startswith("-") or
                    arguments[i].startswith("-")):
                return False
        return True

    def _get_http_method(self, args):
        return args[1] if HTTPMethods.is_method(args[1]) else None

    def _identify_user_request(self, args):
        if (len(args) == 2 and not ServiceCommands.is_command(args[1]) and
                not HTTPMethods.is_method(args[1]) and not args[1].startswith("-") or
                len(args) >= 3 and (HTTPMethods.is_method(args[1]) or
                                    not args[1].startswith("-")) and
                not ServiceCommands.is_command(args[1])):
            return CommandLineHTTPRequest
        else:
            return CommandLineServiceRequest

    def _create_help_user_request(self):
        request = CommandLineServiceRequest()
        request.set_command(ServiceCommands.help_command())
        return request

    def reset_parser(self):
        self._request = None

    @property
    def available_user_request(self):
        return self._request
