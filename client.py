import socket
import sys
import time

x=socket.socket()
h_name= input(str("Enter the hostname of the server: "))
port= 8080
x.connect((h_name,port))
print("Connected to chat server")

while 1: 
   incoming_message=x.recv(1024)
   incoming_messagge=incoming_message.decode()
   print("Server: ", incoming_message.decode())
   message= input(str(">>"))
   Message =message.encode()
   x.send(Message)

input('Press ENTER to exit')
