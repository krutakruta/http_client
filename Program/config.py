class Config:
    _http_methods = {"GET", "POST", "PUT", "DELETE", "OPTIONS",
                     "PATCH", "TRACE", "CONNECT", "HEAD"}

    _service_commands = {"help"}

    @staticmethod
    def http_methods():
        return Config._http_methods

    @staticmethod
    def service_commands():
        return Config._service_commands
