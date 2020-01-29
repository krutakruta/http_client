from functools import wraps


class UserHTTPRequest:
    def __init__(self):
        self.request_method = None
        self.method_argument = None
        self.common_params = {}
        self.method_params = {}
