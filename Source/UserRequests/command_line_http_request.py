from functools import wraps


class CommandLineHTTPRequest:
    def __init__(self):
        self._method = None
        self._method_argument = None
        self._parameters_and_its_option = {}

    def checking_str_arguments(func):
        @wraps(func)
        def wrapper(self, *args):
            for arg in args:
                if not isinstance(arg, str):
                    raise TypeError(
                        "Parameter should be str but it's {}".format(
                            type(arg)))
            func(self, *args)
        return wrapper

    @checking_str_arguments
    def set_parameter_option(self, parameter, option):
        if parameter not in self._parameters_and_options:
            raise KeyError("Can't find {} parameter".format(parameter))
        self._parameters_and_its_option[parameter] = option

    @checking_str_arguments
    def add_method_parameter(self, parameter):
        self._parameters_and_its_option[parameter] = None

    @checking_str_arguments
    def set_method_argument(self, argument):
        self._method_argument = argument

    @checking_str_arguments
    def set_method(self, method):
        self._method = method

    @checking_str_arguments
    def set_parameter_option(self, param, option):
        self._parameters_and_its_option[param] = option

    @property
    def method(self):
        return self._method

    @property
    def parameters_and_its_options(self):
        return self._parameters_and_its_option

    @property
    def method_argument(self):
        return self._method_argument
