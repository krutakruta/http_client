from HTTP.http_response import HTTPResponse


class HTTPResponseParser:
    def parse_response_in_bytes_to_http_response(self, response_in_bytes):
        http_response = HTTPResponse()
        end_of_headers = response_in_bytes.find(b"\r\n\r\n")
        end_of_start_line = response_in_bytes.find(b"\r\n")
        http_response.set_starting_line(
            response_in_bytes[:end_of_start_line].decode("utf-8", errors="ignore"))
        self._parse_headers(
            http_response,
            response_in_bytes[end_of_start_line + 2:end_of_headers].decode(
                "utf-8", errors="ignore"))
        http_response.set_message_body(response_in_bytes[end_of_headers + 10:-7])
        return http_response

    def _parse_headers(self, http_response, text_of_headers):
        for line in text_of_headers.split("\r\n"):
            end_of_header_name = line.find(":")
            http_response.add_header(
                line[:end_of_header_name],
                line[end_of_header_name+2:])
