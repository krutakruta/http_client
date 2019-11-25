from enum import Enum


class HTTP_Methods:

    @staticmethod
    def GET():
        return "GET"

    @staticmethod
    def POST():
        return "POST"

    @staticmethod
    def PUT():
        return "PUT"

    @staticmethod
    def DELETE():
        return "DELETE"

    @staticmethod
    def OPTIONS():
        return "OPTIONS"

    @staticmethod
    def TRACE():
        return "TRACE"

    @staticmethod
    def CONNECT():
        return "CONNECT"

    @staticmethod
    def HEAD():
        return "HEAD"

    @staticmethod
    def PATCH():
        return "PATCH"

    @staticmethod
    def is_method(str_method):
        return str_method in HTTP_Methods._names
