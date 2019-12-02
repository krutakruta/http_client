class ServiceCommands:
    _available_commands = {"help"}

    @staticmethod
    def help_command():
        return "help"

    @staticmethod
    def is_command(c):
        return c in ServiceCommands._available_commands
