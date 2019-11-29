import unittest
from Source.Program.command_line_args_parser import CommandLineArgsParser
from Source.Service.service_commands import ServiceCommands


class TestCommandLineArgsParser(unittest.TestCase):
    def setUp(self):
        self.parser = CommandLineArgsParser()

    def tearDown(self):
        self.parser.reset_parser()

    def test_reset_parser(self):
        self.parser.parse(["main.py", "help"])
        self.parser.reset_parser()
        self.assertEqual(None, self.parser.available_user_request)

    def test_service_help_request(self):
        request = self.parser.parse(["main.py", "help"])
        self.assertEqual(ServiceCommands.help_command(), request.command)
        self.assertEqual(None, request.parameter)

    def test_service_help_request_with_parameter(self):
        request = self.parser.parse(["main.py", "help", "GET"])
        self.assertEqual(ServiceCommands.help_command(), request.command)

