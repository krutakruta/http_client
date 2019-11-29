from Source.Service.service_commands import ServiceCommands
from Source.Service.service_commands_params import ServiceCommandsParams


class CommandLineServiceRequest:

    def __init__(self):
        self._command = None
        self._parameter = None

    def set_command(self, c):
        self._command = c if ServiceCommands.is_command(c) else None

    def set_parameter(self, p):
        if ServiceCommandsParams.is_help_parameter(p):
            self._parameter = p

    @property
    def command(self):
        return self._command

    @property
    def parameter(self):
        return self._parameter
