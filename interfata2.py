import sys,socket,threading,os
from time import sleep
from tkinter import *
class clientulutuf:
    def __init__(self,user=input('Give name: '),host=input('Give ip: '),port=int(input('Give port: '))):
        #set host, port and user
        self.HOST=host
        self.PORT=port
        self.USER=user
        self.conectsock()
        #set interfata
        self.groot = Tk()
        self.groot.geometry("500x600")
        self.groot.title('Chat')

        self.bsend = Button(self.groot,text="Trimite", command=self.trimitemesaj)
        self.bsend.pack(side="top")
        self.bquit = Button(self.groot,text="Quit", command=self.closesock)
        self.bquit.pack(side="top")

        self.emsg = Entry(self.groot)
        self.emsg.pack()
        self.tbox = Text(self.groot)
        self.tbox.pack(fill=BOTH, expand=YES)
        self.sbar = Scrollbar(self.tbox)
        self.sbar.pack(side=RIGHT, fill=Y)
        self.sbar.config(command=self.tbox.yview)

        self.treciv = threading.Thread(target=self.checkprimit,args=[], daemon=True)
        self.treciv.start()
        self.groot.mainloop()
        
    def trimitemesaj(self):
        msg='[['+self.USER+']]:'+self.emsg.get()
        try:
            self.sock.send(msg.encode())
        except ConnectionError:
            print('Socket error during communication')
            self.sock.close()
            print('Closed connection to server\n')
        self.emsg.delete(0,END)

    def conectsock(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.HOST, self.PORT))
        except ConnectionError:
            print('Socket error on connection')
            exit()
    
        print('\nConnected to {}:{}'.format(self.HOST, self.PORT))
        print("Type message, enter to send, 'q' to quit")

    def checkprimit(self):
        self.tbox.insert(INSERT,'\n'+self.primestemesaj())
        sleep(1)
        self.checkprimit()
    
    def closesock(self):
        self.sock.close() 
        exit()

    def primestemesaj(self):
        return self.sock.recv(4048).decode()

x=clientulutuf()
