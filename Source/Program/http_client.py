from Source.Errors.wrong_method_argument_error import WrongMethodArgumentError
from Source.Errors.wrong_parameter_error import WrongParameterError
from Source.HTTP.http_request import HTTPRequest
from Source.Program.command_line_args_parser import CommandLineArgsParser
from Source.UserRequests.command_line_service_request import CommandLineServiceRequest
from urllib.parse import urlparse


class HTTPClient:
    def __init__(self):
        self._command_line_args_parser = CommandLineArgsParser()
        self._http_response = None
        self._http_request = None

    def run(self, args):
        user_request = self._command_line_args_parser.parse(args)
        print(type(user_request))
        if isinstance(user_request, CommandLineServiceRequest):
            print(user_request.command, user_request.parameter)
            self._response = self._create_service_response(user_request)
        else:
            print(user_request)
            print(user_request.method, user_request.parameters_and_its_options,
                  user_request.method_argument)
            try:
                self._check_user_request(user_request)
                self._http_request = self._create_http_request(user_request)
            except WrongParameterError:
                print("param error")

    def _check_user_request(self, user_request):
        self._check_method_argument(user_request)
        self._check_method_parameters(user_request)

    def _check_method_argument(self, user_request):
        parse_result = urlparse(user_request.method_argument)
        if parse_result.scheme == "" or parse_result.netloc == "":
            raise WrongMethodArgumentError(
                "{} isn't url".format(user_request.method_argument))

    def _check_method_parameters(self, user_request):
        pass

    def _create_http_request(self, user_request):
        request = HTTPRequest()


    def _create_service_response(self, user_request):
        pass
