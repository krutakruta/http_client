from Program.config import Config


class Helper:

    @staticmethod
    def is_http_method(method):
        return method in Config.http_methods()

    @staticmethod
    def is_service_command(command):
        return command in Config.service_commands()
