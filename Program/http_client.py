from Errors.errors import *
from HTTP.HTTP_config import HTTPConfig
from HTTP.http_methods import HTTPMethods
from HTTP.http_methods_params import HTTPMethodsParams
from HTTP.http_request import HTTPRequest
from HTTP.http_response import HTTPResponse, HTTPStatus
from Program.client_response import TextClientResponse
from Program.http_response_parser import HTTPResponseParser
from urllib.parse import urlparse
import socket
import re
from HTTP.user_request import UserHTTPRequest


class HTTPClient:
    def __init__(self):
        self._http_response_parser = HTTPResponseParser()
        self._client_response = None
        self._user_request = UserHTTPRequest()
        self._response_to_user = None

    def run(self, args):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                http_response = self._handle_user_request(args, sock)
                #print(http_response.message_body.decode(encoding="utf-8", errors="ignore"))
                self._handle_server_reponse(http_response, sock)
        except Exception:
            raise

    def _handle_user_request(self, args, sock):
        self._parse_args(args)
        if self._user_request.request_method == HTTPMethods.GET:
            http_request = self._create_get_request(self._user_request.method_argument)
            self._send_http_request(http_request, sock)
        else:
            raise WrongMethodError()
        response_in_bytes = self._get_server_response_in_bytes(sock)
        http_response = self._http_response_parser. \
            parse_response_in_bytes_to_http_response(response_in_bytes)
        return http_response

    def _handle_server_reponse(self, http_response, sock):
        if http_response.status == HTTPStatus.Informational:
            self._handle_informational_response(http_response)
        if http_response.status == HTTPStatus.Success:
            self._handle_success_response(http_response)
        if http_response.status == HTTPStatus.Redirection:
            self._handle_redirection_response(http_response, sock)
        if http_response.status == HTTPStatus.Client_error:
            self._handle_client_error_response(http_response)
        if http_response.status == HTTPStatus.Server_error:
            self._handle_server_error_response(http_response)

    def _send_http_request(self, request, sock):
        sock.settimeout(self._user_request.common_params["max_time"])
        sock.connect((request.headers["Host"], 80))
        sock.send(request.request_to_bytes())

    #region processing_response

    def _handle_informational_response(self, http_response):
        pass

    def _handle_success_response(self, http_response):
        if "output" in self._user_request.method_params:
            self._write_message_body_to_file(http_response)
        else:
            self._create_success_response_to_user(http_response)

    def _handle_redirection_response(self, http_request, sock):
        while http_request.status == HTTPResponse.redirection():
            if not self._is_it_correct_url(
                    http_request.headers["Location"]):
                raise WrongUrlError("Redirect url isn't correct")
            sock.connect((self._http_response.headers["Location"], 80))
            if self._user_request.request_method == HTTPMethods.GET:
                self._create_get_request(self._http_response.headers["Location"])
            self._send_http_request(self._http_request, sock)

    def _handle_client_error_response(self, http_response):
        pass

    def _handle_server_error_response(self, http_response):
        pass

    #endregion

    def _write_message_body_to_file(self, http_response):
        try:
            with open(self._user_request.method_params["output"], "w") as file:
                file.write(http_response.message_body)
        except PermissionError:
            raise AccessToTheFileIsDenied(self._method_params["output"])

    def _create_success_response_to_user(self, http_response):
        if http_response.headers["Content-Type"][0] == "text/html":
            self._client_response = TextClientResponse()
            self._decode_message_body()
            self._client_response.set_text(http_response.message_body)

    def _decode_message_body(self):
        charset = self._get_charset_from_http_response()
        self._http_response.set_message_body(
            self._http_response.message_body.decode(charset, errors="ignore"))

    def _get_charset_from_http_response(self):
        for option in self._http_response.headers["Content-Type"]:
            if option.find("charset") != -1:
                return re.sub(r"[\"\']", "", option.split("=")[1]).lower()

    def _get_server_response_in_bytes(self, sock):
        MTU = 4096
        bytes_pack = sock.recv(MTU)
        response = bytes_pack
        try:
            while bytes_pack != b"":
                bytes_pack = sock.recv(MTU)
                response += bytes_pack
        finally:
            return response

    def _parse_args(self, args):
        self._check_correctness_of_args(args)
        self._extract_params_from_args(args)
        self._user_request.method_argument = args.url
        self._user_request.request_method = args.request_method

    def _extract_params_from_args(self, parsed_args):
        for param, options in vars(parsed_args).items():
            if options is not None:
                if HTTPMethodsParams.is_common_param(param):
                    self._user_request.common_params[param] = options
                elif HTTPMethodsParams.is_GET_param(param):
                    self._user_request.method_params[param] = options

    def _create_get_request(self, url, headers=None,
                            http_version=HTTPConfig.default_http_version()):
        http_request = HTTPRequest()
        headers = (self._create_default_headers(url) if headers is None
                   else headers)
        parsed_url = urlparse(url)
        self._set_starting_line_for_request(
            http_request,
            (parsed_url.path
             if parsed_url.path != "" and parsed_url.netloc != ""else "/"),
            http_version)
        self._set_headers_for_request(http_request, headers)
        return http_request

    def _set_starting_line_for_request(self, request,
                                       path_on_website, http_version):
        request.starting_line =\
            "{} {} HTTP/{}".format(self._user_request.request_method,
                                   path_on_website, http_version)

    def _set_headers_for_request(self, http_request, headers):
        for header, option in headers.items():
            http_request.headers[header] = option

    def _create_default_headers(self, url):
        parsed_url = urlparse(url)
        headers = {"Host": (parsed_url.netloc if parsed_url.netloc != ""
                            else parsed_url.path),
                   "Accept": ", ".join(HTTPConfig.accept_mime_types()),
                   "User-Agent": HTTPConfig.client_name()}
        if "addition_header" in self._user_request.common_params:
            for header_and_option in self._common_params["additional_header"]:
                headers[header_and_option[0]] = header_and_option[1]
        return headers

    def _check_correctness_of_args(self, parsed_args):
        parsed_url = urlparse(parsed_args.url)
        print(parsed_url)
        if ((parsed_url.scheme != "http" or parsed_url.netloc == "") and
                parsed_url.path == ""):
            raise WrongUrlError(parsed_args.url)
        if parsed_args.request_method == HTTPMethods.GET:
            self._check_correctness_of_get_method_parameters(parsed_args)

    def _check_correctness_of_get_method_parameters(self, parsed_args):
        for arg, opt in vars(parsed_args).items():
            if opt is not None and arg != "request_method" and arg != "url":
                if (not (HTTPMethodsParams.is_common_param(arg) or
                         HTTPMethodsParams.is_GET_param(arg))):
                    raise WrongMethodParameterError(arg)

    def _check_user_request(self, user_request):
        if not self._is_it_correct_url(user_request.method_argument):
            raise WrongUrlError(
                "{} isn't http url".format(user_request.method_argument))
        self._check_method_parameters(user_request)

    def _is_it_correct_url(self, url):
        parse_result = urlparse(url)
        return not (parse_result.scheme != "http" or
                    parse_result.netloc == "" or
                    url != "localhost")

    def _check_method_parameters(self, user_request):
        if user_request.method == HTTPMethods.GET:
            for param in user_request.parameters_and_its_options_copy:
                if not HTTPMethodsParams.is_GET_param(param):
                    raise WrongMethodParameterError(
                        "{} isn't {}'s parameter".format(
                            param, user_request.method))

    def get_client_response(self):
        return self._client_response
