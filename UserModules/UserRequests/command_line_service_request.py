class CommandLineServiceRequest:

    def __init__(self, user_request):
        self._user_request = user_request
        self._command = None
        self._parameter = None
