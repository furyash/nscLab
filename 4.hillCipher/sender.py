import socket
import random

port = 4545
format = 'utf-8'
size  = 1024
server = socket.socket()
host = socket.gethostname()
server.bind((host,port))

message = input("Enter a message to send : ").lower().replace(' ','')
key = input("Provide a key (min. 9ltrs) :").lower()

def formatting(message):
    lst = list(message)
    if len(lst)%3 ==1:
        lst.append('x')
    if len(lst)%3 ==2:
        lst.append('x')
    return ''.join(lst)


def encrypt(message,key):
    cypherT = ''
    for i in range(0,len(message)-1,3):
        cypherT+=(shrt_crypt(message[i:i+3],key))
    return cypherT

def shrt_crypt(mesg,key):
    a = chr(97+(key[0][0] * mesg[0] + key[0][1] * mesg[1] + key[0][2] * mesg[2]) % 26)
    b = chr(97+(key[1][0] * mesg[0] + key[1][1] * mesg[1] + key[1][2] * mesg[2]) % 26)
    c = chr(97+(key[2][0] * mesg[0] + key[2][1] * mesg[1] + key[2][2] * mesg[2]) % 26)
    return ''.join([a,b,c])

message = formatting(message)
message = [ord(x)-97 for x in message]
key = [ord(x)-97 for x in key]
key = [key[:3],key[3:6],key[6:9]]
print(message)
message = encrypt(message,key)
print(key)
print(message)



server.listen()
print("\nSending Message...")
conn, addr = server.accept()
conn.send((message).encode(format))

print(f"Encryted Message Sent to [{addr}].")
conn.close()
server.close()

