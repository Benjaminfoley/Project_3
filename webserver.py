import socket
import sys

#Server Side


#create a socket using user inputs for website and port
s = socket.socket()
user_input = sys.argv[1]
s.bind(('',int(user_input)))

#listen for incoming connection
s.listen()
print(f'Listening... on host {user_input}',)
data = b""
while True:
        connection = s.accept()
        print(connection)
        new_socket = connection[0]  # This is what we'll recv/send on
    #Accept incoming connection
        while True:
            data = new_socket.recv(4096)

            if b"\r\n\r\n" in data:
                break
        print(data.decode("ISO-8859-1"))
        ht = "HTTP/1.1 200 OK\r\n\
        You are awake"
        enht = ht.encode("ISO-8859-1")
        new_socket.sendall(enht)



    # while True:
    #     print(data.decode("ISO-8859-1"))
        # data = s.recv(4096)



        new_socket.close()

        #PROJECT 3

        required_text = ('GET /file1.txt HTTP/1.1\r\n')
        required_text.split(" ")

        # GET_finder = ht.find("GET")
        # GET_finder.split(GET_finder = "Get")

       # Stripping the pth down
       os.path.split("file1.txt") 

       #MIME 
       Content-Type: text/plain; charset=iso-8859-1


       #READing file
       try:
            with open(filename) as fp:
                data = fp.read()   # Read entire file
                return data

        except:
            # File not found or other error
            # TODO send a 404





        