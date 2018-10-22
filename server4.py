import sys,socket,threading
class serverulutuf:
    RECV_BUFFER=4096

    def __init__(self,host='localhost',port=9000):
        self.HOST=host
        self.PORT=port
        self.SOCKET_LIST=[]
	
    def handle_client(self,sock, addr):
        while True:
            try:
                msg=sock.recv(4048)
                print(msg.decode())
                for s in self.SOCKET_LIST:
                    #if(s!=sock):
                    s.send(msg)
            except (ConnectionError, BrokenPipeError):
                print('Closed connection to {}'.format(addr))
                self.SOCKET_LIST.remove(sock)
                sock.close()
                break

    def chat_server(self):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen(10)

        print ("Chat server started on port " + str(self.PORT))

        while True:
        # accept connections from outside
            (soc, address) = server_socket.accept()
            self.SOCKET_LIST.append(soc)
            thread = threading.Thread(target = self.handle_client, args = [soc, address], daemon=True)
            thread.start()
        s.close()

ser=serverulutuf()
ser.chat_server()
