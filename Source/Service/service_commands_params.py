class ServiceCommandsParams:
    _available_commands_params = {"help": ("GET", "POST", "PUT", "DELETE",
                                           "OPTIONS", "PATCH", "TRACE",
                                           "CONNECT", "HEAD")}

    @staticmethod
    def is_help_parameter(p):
        return p in ServiceCommandsParams._available_commands_params["help"]
