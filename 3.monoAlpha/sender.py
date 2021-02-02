import socket
import random

port = 4545
format = 'utf-8'
size  = 1024
server = socket.socket()
host = socket.gethostname()
server.bind((host,port))

message = input("Enter a message to send : ").lower().replace(' ','')

def encrypt(key, message):
    cypherT = []
    #alpha = [chr(n) for n in range(97,123)]
    for i in range(len(message)):
        #print(97 - ord(message[i]))
        c = key[ord(message[i])-97]
        cypherT.append(c)
    return ''.join(cypherT)

key = [chr(n) for n in range(97,123)]  # general alphabets
random.shuffle(key)
key = ''.join(key)
print("Key : ",key)
message = encrypt(key,message)

server.listen()
print("\nSending Message...")
conn, addr = server.accept()
conn.send((message).encode(format))
conn.send((key).encode(format))
print(f"Encryted Message Sent to [{addr}].")
conn.close()
server.close()
