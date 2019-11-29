from Source.HTTP.http_methods import HTTPMethods


class StartingLine:
    def __init__(self, method=None, URI=None, http_version=None):
        self._check_method(method)
        self._method = method
        self._URI = URI
        self._http_version = http_version

    def _check_method(self, method):
        if type(method) is not HTTPMethods:
            raise TypeError("{} isn't command type".format(type(method)))
