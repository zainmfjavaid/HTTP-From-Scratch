import socket

def _parse_raw_http_response(raw_response: bytes) -> dict:
    response_info, payload = raw_response.decode().split('\r\n\r\n')
    response_line = response_info.split('\r\n')[0]
    
    response_code = ' '.join(response_line.split()[1:])
    
    return {'status':response_code, 'content':payload}

def construct_http_string(http_method: str, host_name: str, body: dict) -> str:
    host_name = host_name.replace('http://', '')
    
    port = 80
    if ':' in host_name:
        host_name, port = host_name.split(':')
        port = int(port)
    
    parts = host_name.split('/')
    host_url, uri = parts[0], '/'+'/'.join(parts[1:])
    host = socket.gethostbyname(host_url)
    
    http_string = f'{http_method} {uri} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n'
    if body:
        http_string += str(body)
    return http_string, host, uri, port

def send(http_string: str, host: str, port: int) -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(http_string.encode('utf-8'))
        data = s.recv(1024)
    return _parse_raw_http_response(data)