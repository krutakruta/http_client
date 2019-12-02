from enum import Enum


class HTTPMethods:
    _available_methods = {"GET"}

    _potential_methods = {"POST", "PUT", "DELETE", "OPTIONS",
                          "PATCH", "TRACE", "CONNECT", "HEAD"}

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    CONNECT = "CONNECT"
    TRACE = "TRACE"
    HEAD = "HEAD"
    PATCH = "PATCH"
    PUT = "PUT"
    OPTIONS = "OPTIONS"

    @staticmethod
    def is_method(m):
        return m in HTTPMethods._available_methods
