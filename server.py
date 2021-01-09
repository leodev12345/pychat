import socket
import sys
import time
import threading


x = socket.socket()
h_name= socket.gethostname()
print("server will start on host: ", h_name)
port= 1234
x.bind((h_name, port))
print( "server done binding to host and port successfully")
print("server is waiting for incoming connections")
x.listen()
connection,address= x.accept()
print(address, " Has connected to the server and is now online...")
print("You can now start sending messages")

def send():
   while 1: 
      display_mess= input(str())   
      display_mess=display_mess.encode()
      connection.send(display_mess)

def recv():
   while 1:
      in_message=connection.recv(1024)
      in_messagge=in_message.decode()
      print("Client:", in_message.decode())

threading.Thread(target=send).start()
threading.Thread(target=recv).start()

