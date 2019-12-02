import sys
from Program.http_client import HTTPClient
import argparse


# ["main.py", "help", "GET"]
# ["main.py", "dsf", "-o", "http://vk.com", "sdasd"]


def main():
    http_client = HTTPClient()
    args_parser = create_parser()
    try:
        parsing_result = args_parser.parse_args()
        http_client.run(parsing_result)
    except Exception:
        raise

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X", "--request-method", default="GET",
        type=str, help="HTTP request method")
    parser.add_argument(
        "-o", "--output", type=str, help="Output file")
    parser.add_argument(
        "-m", "--max-time", type=int,
        help="Maximum time allowed for the transfer")
    parser.add_argument("url")
    return parser


if __name__ == "__main__":
    main()
