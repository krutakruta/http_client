class HTTPMethodsParams:
    _http_methods_params = {"GET": {"remote_name": "-O", "output": "-o"}}
    _common_http_method_params = {"max_time": "-m", "additional_header": "-hr"}

    @staticmethod
    def is_GET_param(p):
        return p in HTTPMethodsParams._http_methods_params["GET"]

    @staticmethod
    def is_common_param(p):
        return p in HTTPMethodsParams._common_http_method_params
