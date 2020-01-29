class WrongUrlError(Exception):
    pass

class WrongMethodError(Exception):
    pass


class WrongMethodParameterError(Exception):
    pass


class WrongParameterOptionError(Exception):
    pass


class WrongHTTPResponseError(Exception):
    pass

class AccessToTheFileIsDenied(Exception):
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename
