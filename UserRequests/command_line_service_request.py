from Service.service_commands import ServiceCommands
from Service.service_commands_params import ServiceCommandsParams


class CommandLineServiceRequest:

    def __init__(self):
        self._command = None
        self._argument = None

    def set_command(self, c):
        self._command = c if ServiceCommands.is_command(c) else None

    def set_parameter(self, p):
        if ServiceCommandsParams.is_help_parameter(p):
            self._argument = p

    @property
    def command(self):
        return self._command

    @property
    def argument(self):
        return self._argument
