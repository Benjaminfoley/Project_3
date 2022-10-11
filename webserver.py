import socket
import sys
import os

#Server Side


#create a socket using user inputs for website and port
s = socket.socket()
user_input = sys.argv[1]
s.bind(('',int(user_input)))

#listen for incoming connection
s.listen()
print(f'Listening... on host {user_input}',)
map_ext =  {'.txt': 'text/plain', '.ico': 'image/x-icon', '.html': 'text/html'}
def get_request(new_socket):
    data = new_socket.recv(4096)
    result = ""
    while True:
        result = result + data.decode("ISO-8859-1")
        
        if b"\r\n\r\n" in data:
            return result
        print(result)
        data = new_socket.recv(4096)

while True:
    #Accept incoming connection
    connection = s.accept()
    print(connection)
    new_socket = connection[0]  # This is what we'll recv/send on
    client_req = get_request(new_socket)


    #PROJECT 3

    parse_request = client_req.split('\r\n')
    request_method = parse_request[0].split()[0]
    request_path = parse_request[0].split()[1]
    request_protocol = parse_request[0].split()[2]
    file_path_tuple = os.path.split(request_path)
    file_name = file_path_tuple[1]
    file_extension_tuple = os.path.splitext(file_name)
    file_extension = file_extension_tuple[1]


    #READing file
    content_type = map_ext[file_extension]
    try:
        with open(file_name) as fp:
            body = fp.read()   # Read entire file
            content_length = len(body)
            response = 'HTTP/1.1 200 OK\r\n\
        Content-Type: {}\r\n\
        Content-Length: {}\r\n\
        Connection: close\r\n\r\n\
        {}'.format(content_type, content_length, body).encode("ISO-8859-1")
        new_socket.sendall(response)
    except:
        response = 'HTTP/1.1 404 Not Found\r\n\
        Content-Type: {}\r\n\
        Content-Length: 13\r\n\
        Connection: close\r\n\r\n\
        404 not found'.format(content_type).encode("ISO-8859-1")
        new_socket.sendall(response)
    new_socket.close()