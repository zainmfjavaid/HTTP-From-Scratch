from utils import send, construct_http_string

def _request(http_method: str, host_name: str, message_body: dict) -> dict:
    http_string, host, _, port = construct_http_string(http_method, host_name, message_body)
    return send(http_string, host, port)

def get(host_name: str, message_body: dict) -> dict:
    return _request('GET', host_name, message_body)

def post(host_name: str, message_body: dict) -> dict:    
    return _request('POST', host_name, message_body)

def put(host_name: str, message_body: dict) -> dict:    
    return _request('PUT', host_name, message_body)

def delete(host_name: str, message_body: dict) -> dict:    
    return _request('DELETE', host_name, message_body)

if __name__ == '__main__':
    url = 'http://httpbin.org/'
    message_body = {}
    
    print(get(url, message_body))