import sys
from Program.http_client import HTTPClient


def main():
    program = HTTPClient()
    print(sys.argv)
    program.run(sys.argv)


if __name__ == "__main__":
    main()