import socket
import random

port = 4545
format = 'utf-8'
size  = 1024
server = socket.socket()
host = socket.gethostname()
server.bind((host,port))

message = input("Enter a message to send : ").lower().replace(' ','')
key = input("Enter a key : ")
sKey = sorted(key)


leng = len(key)
width = len(message)
if width % leng != 0:
    message = list(message)
    for i in range(leng - (width % leng)):
        message.append('x')
    message = ''.join(message)


tb =[[] for x in range(leng)]
for i in range(leng):
    for j in range(len(message)//leng):
        pos = sKey.index(key[i])
        tb[pos].append(message[i + j*leng])
        pass
ciphTex = ''.join([y for x in tb for y in x])

server.listen()
print("\nSending Message...")
conn, addr = server.accept()
conn.send((ciphTex).encode(format))

print(f"Encryted Message Sent to [{addr}].")

conn.close()
server.close()


