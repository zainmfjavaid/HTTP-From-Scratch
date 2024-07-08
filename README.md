# HTTP From Scratch
Source code for [this blog post](https://zainj.dev/posts?post=recreating-http) about recreating HTTP in
Python using only the `socket` and `json` libraries in Python.

## Setup
Clone the repo:

```
git clone https://github.com/zainmfjavaid/HTTP-From-Scratch
```

## Running the client

```
cd client
python client.py
```

This will send a `GET` request to the httpbin.org website by default. To change this, edit these lines
in the client.py file:

```python
if __name__ == '__main__':
    url = 'http://httpbin.org/' # Replace with your host
    message_body = {} # Replace with your message body
    
    print(get(url, message_body)) # Replace get with your HTTP method
```

Alternatively, you can import the client code as a module and use it that way:

```python
from client import get, post, put, delete

message_body = {}

get('http://httpbin.org/', message_body)
post('http://httpbin.org/post', message_body)
put('http://httpbin.org/put', message_body)
delete('http://httpbin.org/delete', message_body)
```

## Running the server

```
cd server
python server.py
```

This will start host the server at `127.0.0.1` on port `65432`. To verify that the server is running,
you can type `127.0.0.1:65432/` into your browser or send it requests using the client.