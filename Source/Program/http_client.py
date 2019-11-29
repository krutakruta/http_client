from Source.Errors.wrong_method_argument_error import WrongMethodArgumentError
from Source.Errors.wrong_parameter_error import WrongParameterError
from Source.HTTP.http_methods import HTTPMethods
from Source.HTTP.http_methods_params import HTTPMethodsParams
from Source.HTTP.http_request import HTTPRequest
from Source.Program.command_line_args_parser import CommandLineArgsParser
from Source.UserRequests.command_line_service_request import CommandLineServiceRequest
from urllib.parse import urlparse
import socket


class HTTPClient:
    def __init__(self):
        self._command_line_args_parser = CommandLineArgsParser()
        self._http_response = None
        self._http_request = None

    def run(self, args):
        user_request = self._command_line_args_parser.parse(args)
        print(type(user_request))
        if isinstance(user_request, CommandLineServiceRequest):
            print(user_request.command, user_request.argument)
            self._response = self._create_service_response(user_request)
        else:
            print(user_request)
            print("Method", user_request.method, user_request.parameters_and_its_options_copy,
                  "\nArgument", user_request.method_argument)
            try:
                self._check_user_request(user_request)
                self._http_request = self._create_http_request(user_request)
                self._send_http_request()
            except WrongMethodArgumentError:
                print("_________Argument error__________")
            except WrongParameterError:
                print("_________Parameter error__________")

    def _send_http_request(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self._http_request.headers["Host"], 80))
            sock.send(self._http_request.create_request_text().encode())
            result = sock.recv(2048)
            print(result.decode("utf-8", errors="ignore"))


    def _check_user_request(self, user_request):
        self._check_method_argument(user_request)
        self._check_method_parameters(user_request)

    def _check_method_argument(self, user_request):
        parse_result = urlparse(user_request.method_argument)
        if parse_result.scheme != "http" or parse_result.netloc == "":
            raise WrongMethodArgumentError(
                "{} isn't url".format(user_request.method_argument))

    def _check_method_parameters(self, user_request):
        if user_request.method == HTTPMethods.get_method():
            for param in user_request.parameters_and_its_options_copy:
                if not HTTPMethodsParams.is_GET_param(param):
                    raise WrongParameterError(
                        "{} isn't {}'s parameter".format(
                            param, user_request.method))

    def _create_http_request(self, user_request):
        http_request = HTTPRequest()
        self._set_starting_line(http_request, user_request)
        self._set_headers(http_request, user_request)
        self._set_message_body(http_request, user_request)
        return http_request

    def _set_starting_line(self, http_request, user_request):
        url_parse_result = urlparse(user_request.method_argument)
        http_request.set_starting_line(
            "{} {} HTTP/1.1".format(user_request.method, url_parse_result.path))

    def _set_headers(self, http_request, user_request):
        url_parse_result = urlparse(user_request.method_argument)
        http_request.add_header("Host", url_parse_result.netloc)

    def _set_message_body(self, http_request, user_request):
        pass

    def _create_service_response(self, user_request):
        pass
