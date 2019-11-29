class WrongMethodArgumentResponse:
    def __init__(self, method, argument):
        self._method = method
        self._argument = argument
