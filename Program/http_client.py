from Errors.wrong_arguments_errors import WrongMethodArgumentError, WrongMethodParameterError, WrongMethodError
from HTTP.HTTP_config import HTTPConfig
from HTTP.http_methods import HTTPMethods
from HTTP.http_methods_params import HTTPMethodsParams
from HTTP.http_request import HTTPRequest
from UserRequests.command_line_service_request import CommandLineServiceRequest
from urllib.parse import urlparse
import socket


class HTTPClient:
    def __init__(self):
        self._http_response = None
        self._http_request = None
        self._request_method = None
        self._common_params = {}
        self._method_params = {}
        self._method_arg = None

    def run(self, parsed_args):
        self._handle_parsed_args(parsed_args)
        if parsed_args.request_method == HTTPMethods.GET:
            self._create_get_request()
            self._send_http_request()
        else:
            raise WrongMethodError()

    def _send_http_request(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self._http_request.headers["Host"], 80))
            sock.send(self._http_request.request_to_bytes())
            self._get_server_response_by_socket(sock)
            result = sock.recv(256)
            print(result.decode("utf-8", errors="ignore"))
            result = sock.recv(256)
            print(result.decode("utf-8", errors="ignore"))

    def _get_server_response_by_socket(self, sock):
        num_of_bytes = 512
        part_of_response = sock.recv(num_of_bytes).decode(
            "utf-8", errors="ignore")
        parts_of_response = [part_of_response]
        while part_of_response != "":
            part_of_response.append(sock.recv(num_of_bytes).decode(
                "utf-8", errors="ignore"))
        self._http_response = "".join(part_of_response)

    def _handle_parsed_args(self, parsed_args):
        self._check_correctness_of_parsed_args(parsed_args)
        self._extract_params_from_parsed_args(parsed_args)
        self._method_arg = parsed_args.url
        self._request_method = parsed_args.request_method

    def _extract_params_from_parsed_args(self, parsed_args):
        for param, options in vars(parsed_args).items():
            if options is not None:
                if HTTPMethodsParams.is_common_param(param):
                    self._common_params[param] = options
                elif HTTPMethodsParams.is_GET_param(param):
                    self._method_params[param] = options

    def _create_get_request(self):
        self._http_request = HTTPRequest()
        parsed_url = urlparse(self._method_arg)
        self._set_starting_line(
            parsed_url.path if parsed_url.path != "" else "/",
            HTTPConfig.default_http_version())
        self._set_headers()

    def _set_starting_line(self, path_on_website, http_version):
        self._http_request.set_starting_line(
            "{} {} HTTP/{}".format(self._request_method, path_on_website, http_version))

    def _set_headers(self):
        url_parse_result = urlparse(self._method_arg)
        self._http_request.add_header("Host", url_parse_result.netloc)

    def _set_message_body(self, http_request, user_request):
        pass

    def _check_correctness_of_parsed_args(self, parsed_args):
        parsed_url = urlparse(parsed_args.url)
        if parsed_url.scheme != "http" or parsed_url.netloc == "":
            raise WrongMethodArgumentError(
                parsed_args.request_method,
                parsed_url.scheme if parsed_url.scheme != "http"
                else parsed_url.netloc)
        if parsed_args.request_method == HTTPMethods.GET:
            self._check_correctness_of_get_method_parameters(parsed_args)

    def _check_correctness_of_get_method_parameters(self, parsed_args):
        for arg, opt in vars(parsed_args).items():
            if opt is not None and arg != "request_method" and arg != "url":
                if (not (HTTPMethodsParams.is_common_param(arg) or
                         HTTPMethodsParams.is_GET_param(arg))):
                    raise WrongMethodParameterError()

    def _create_service_response(self, user_request):
        pass

    def _check_user_request(self, user_request):
        self._check_method_argument(user_request)
        self._check_method_parameters(user_request)

    def _check_method_argument(self, user_request):
        parse_result = urlparse(user_request.method_argument)
        if parse_result.scheme != "http" or parse_result.netloc == "":
            raise WrongMethodArgumentError(
                "{} isn't url".format(user_request.method_argument))

    def _check_method_parameters(self, user_request):
        if user_request.method == HTTPMethods.GET:
            for param in user_request.parameters_and_its_options_copy:
                if not HTTPMethodsParams.is_GET_param(param):
                    raise WrongMethodParameterError(
                        "{} isn't {}'s parameter".format(
                            param, user_request.method))
