import socket
import routes
from utils import *

HOST = '127.0.0.1'
PORT = 65432

uri_mapping = {'/': routes.index, '/accounts':routes.accounts}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    while True:
        conn, addr = s.accept()
        with conn:
            http_request = conn.recv(2048).decode()
                        
            http_method, uri, request_body = parse_http_request(http_request)
            output = uri_mapping.get(uri, routes.page_not_found)(http_method, request_body)
            
            if not http_request:
                break
            conn.sendall(construct_http_response(output['status'], output['body']).encode('utf-8'))