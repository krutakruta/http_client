import socket
import sys
from Program.http_client import HTTPClient
from Errors.errors import *
import argparse


# ["main.py", "help", "GET"]
# ["main.py", "dsf", "-o", "http://vk.com", "sdasd"]


def main():
    http_client = HTTPClient()
    args_parser = create_parser()
    try:
        parsing_result = args_parser.parse_args()
        http_client.run(parsing_result)
        response = http_client.get_client_response()
        if response is not None:
            print_client_response(response)
    except socket.gaierror:
        print("Сервер недоступен")
    except AccessToTheFileIsDenied as error:
        print("Доступ к файлу {} запрещен".format(error.filename))
    except Exception:
        raise


def print_client_response(response):
    print(response.text)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X", "--request-method", default="GET",
        type=str, help="HTTP request method")
    parser.add_argument(
        "-o", "--output", type=str, help="Output file")
    parser.add_argument(
        "-m", "--max-time", type=float, default=0.2,
        help="Maximum time allowed for the transfer")
    parser.add_argument("url")
    return parser


if __name__ == "__main__":
    main()
