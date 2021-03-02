from tkinter import *
from tkinter import messagebox
from client import Client

class ClientGraphique():
    def __init__(self):
        super(Client, self).__init__()
        self.root = Tk()
        self.root.title('Messagerie Instantanee')
        self.canevas = Canvas(self.root, width = 300, height = 300, background= '#000')
        self.canevas.pack()
        self.canevas.bind('<Button-1>' , self.gestion_clic)
        self.initGrid()
        self.root.mainloop()
if __name__ == "__main__":
    username= input("username: ")
    server= input("server: ")
    port= int(input("port: "))
    client= Client(username, server, port)
    clientgraphique= (client)
    clientgraphique.listen()
    message= ""
    while message!="QUIT":
        message= input()
        clientgraphique.send(message)   