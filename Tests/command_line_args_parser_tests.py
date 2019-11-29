import unittest

from Source.HTTP.http_methods import HTTPMethods
from Source.Program.command_line_args_parser import CommandLineArgsParser
from Source.Service.service_commands import ServiceCommands


class TestCommandLineArgsParser(unittest.TestCase):
    def setUp(self):
        self.parser = CommandLineArgsParser()

    def test_reset_parser(self):
        self.parser.parse(["main.py", "help"])
        self.parser.reset_parser()
        self.assertEqual(None, self.parser.available_user_request)

    def test_service_help_request(self):
        request = self.parser.parse(["main.py", "help"])
        self.assertEqual(ServiceCommands.help_command(), request.command)
        self.assertEqual(None, request.argument)

    def test_service_help_request_with_parameter(self):
        request = self.parser.parse(["main.py", "help", "GET"])
        self.assertEqual(ServiceCommands.help_command(), request.command)
        self.assertEqual(HTTPMethods.get_method(), request.argument)

    def test_empty_request(self):
        request = self.parser.parse(["main.py"])
        self.assertEqual(ServiceCommands.help_command(), request.command)

    def test_explicit_get_method(self):
        request = self.parser.parse(
            ["main.py", "GET", "http://anytask.urgu.org/", "-o", "text.txt"])
        self.assertEqual(HTTPMethods.get_method(), request.method)
        self.assertEqual("http://anytask.urgu.org/", request.method_argument)
        self.assertEqual(
            "text.txt", request.parameters_and_its_options_copy["-o"])

    def test_not_explicit_get_method(self):
        request = self.parser.parse(
            ["main.py", "http://anytask.urgu.org/", "-o", "text.txt"])
        self.assertEqual(HTTPMethods.get_method(), request.method)
        self.assertEqual("http://anytask.urgu.org/", request.method_argument)
        self.assertEqual(
            "text.txt", request.parameters_and_its_options_copy["-o"])



