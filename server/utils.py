import json

def parse_http_request(http_string: str) -> tuple:
    request_info, request_body = http_string.split('\r\n\r\n')
    request_line = request_info.split('\r\n')[0]
    
    if request_body:
        request_body = json.loads(request_body.replace("'", '"'))
    else:
        request_body = {}
    
    http_method, uri, _ = request_line.split()
    return http_method, uri, request_body

def construct_http_response(status: str, response_data: dict) -> str:
    return f'HTTP/1.1 {status}\r\nContent-Type: application/json\r\n\r\n{response_data}'