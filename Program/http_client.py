from Program.command_line_args_parser import CommandLineArgsParser


class HTTPClient:
    def __init__(self):
        self._command_line_args_parser = CommandLineArgsParser()

    def run(self, args):
        self._command_line_args_parser.parse(args)
