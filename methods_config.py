class MethodsConfig:
    _get_available_parameters = {"-o", "-O", "-m"}

    @staticmethod
    def get_available_parameters():
        return MethodsConfig._get_available_parameters
