import socket
import sys
import time
import threading

x=socket.socket()
h_name= input(str("Enter the hostname of the server: "))
port= 1234
x.connect((h_name,port))
print("Connected to chat server")
print("You can now start sending messages")
def recv():
   while 1: 
      incoming_message=x.recv(1024)
      print("Server: ", incoming_message.decode())

def send():
   while 1:
      message= input(str())
      Message =message.encode()
      x.send(Message)

threading.Thread(target=recv).start()
threading.Thread(target=send).start()




