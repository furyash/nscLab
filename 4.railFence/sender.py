import socket
import random

port = 4545
format = 'utf-8'
size  = 1024
server = socket.socket()
host = socket.gethostname()
server.bind((host,port))

message = input("Enter a message to send : ").lower().replace(' ','')
key = int(input("Enter a key to encrypt : "))

width = len(message)
if width % key != 0:
    message = list(message)
    for i in range(key - (width % key)):
        message.append('x')
    message = ''.join(message)

tb =[[] for x in range(key)]
for i in range(key):
    for j in range(len(message)//key):
        
        tb[i].append(message[i + j*key])
        pass
ciphTex = ''.join([y for x in tb for y in x])

server.listen()
print("\nSending Message...")
conn, addr = server.accept()
conn.send((ciphTex).encode(format))
print(f"Encryted Message Sent to [{addr}].")
conn.close()
server.close()

