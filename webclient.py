import socket
import sys
#Client Side

#Create connection
s = socket.socket()
user_input = sys.argv[1]
port_input = 80
if len(sys.argv) > 2: # check if port is entered
  port_input = int(sys.argv[2]) 
s.connect((user_input,int(port_input)))

request = 'GET / HTTP/1.1\r\n\
Host: %s \r\n\
Connection: close\r\n\
\r\n'%user_input
request = request.encode("ISO-8859-1")

s.sendall(request)

d = s.recv(4096)  # Receive up to 4096 bytes
while len(d) != 0:
    print(d.decode("ISO-8859-1"))
    d = s.recv(4096)
    # all done!

s.close()
#close out of the program