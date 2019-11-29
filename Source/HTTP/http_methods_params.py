class HTTPMethodsParams:
    _http_methods_params = {"GET": {"-o", "-O", "-m"}}

    @staticmethod
    def is_GET_param(p):
        return p in HTTPMethodsParams._http_methods_params["GET"]
