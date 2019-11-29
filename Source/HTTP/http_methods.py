from enum import Enum


class HTTPMethods:
    _available_methods = {"GET", "POST", "PUT", "DELETE", "OPTIONS",
                          "PATCH", "TRACE", "CONNECT", "HEAD"}

    @staticmethod
    def get_method():
        return "GET"

    @staticmethod
    def post_method():
        return "POST"

    @staticmethod
    def put_method():
        return "PUT"

    @staticmethod
    def delete_method():
        return "DELETE"

    @staticmethod
    def options_method():
        return "OPTIONS"

    @staticmethod
    def trace_method():
        return "TRACE"

    @staticmethod
    def connect_method():
        return "CONNECT"

    @staticmethod
    def head_method():
        return "HEAD"

    @staticmethod
    def patch_method():
        return "PATCH"

    @staticmethod
    def is_method(m):
        return m in HTTPMethods._available_methods
