import sys
from Source.Program.http_client import HTTPClient


# ["main.py", "help", "GET"]
# ["main.py", "dsf", "-o", "http://vk.com", "sdasd"]


def main():
    program = HTTPClient()
    program.run(sys.argv)


if __name__ == "__main__":
    main()
