def index(method: str, request_body: dict):
    if method != 'GET':
        return {
            'status':'405 Method Not Allowed',
            'body': {
                'error': 'Method Not Allowed',
                'message': f"The '{method}' method is not supported for this route.",
                'allowed_methods': ['GET']
            }
        }
    
    return {'status': '200 OK', 'body': {'message': 'Success!'}}

def accounts(method: str, request_body: dict):
    if 'username' not in request_body:
        return {
            'status':'400 Bad Request',
            'body': {
                'error': 'Bad Request',
                'message': f"Missing 'username' parameter"
            }
        }
    
    if method == 'GET':
        return {'status': '200 OK', 'body': {'message': f"Getting user info for {request_body['username']}"}}
    elif method == 'POST':
        return {'status': '200 OK', 'body': {'message': f"Creating profile for {request_body['username']}"}}
    elif method == 'PUT':
        return {'status': '200 OK', 'body': {'message': f"Updating profile for {request_body['username']}"}}
    elif method == 'DELETE':
        return {'status': '200 OK', 'body': {'message': f"Deleting profile for {request_body['username']}"}}
    else:
        return {
            'status':'405 Method Not Allowed',
            'body': {
                'error': 'Method Not Allowed',
                'message': f"The '{method}' method is not supported for this route.",
                'allowed_methods': ['GET', 'POST', 'PUT', 'DELETE']
            }
        }
        
def page_not_found(*args):
    return {
            'status':'404 Not Found',
            'body': {
                'error': 'Not Found',
                'message': f"Couldn't find requested resource on server."
            }
        } 