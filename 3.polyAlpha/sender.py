import socket

port = 4545
format = 'utf-8'
size  = 1024
server = socket.socket()
host = socket.gethostname()
server.bind((host,port))

message = input("Enter a message to send : ").lower().replace(' ','')
key = input("Enter key to encrypt : ").lower()

def keyExtend(shrt_key,message):
    key=[]
    width = len(message)
    i=0
    while i <width :
        for s in shrt_key:
            key.append(s)
            i+=1
            if not i < width:
                break
    return ''.join(key)

def encrypt(key, message):
    cypherT = []
    alpha = [chr(n) for n in range(97,123)]
    for i in range(len(message)):
        a= key[i]
        b= message[i]
        c = chr(97+(((97-ord(a)) + (97-ord(b)))%26))
        cypherT.append(c)
    return ''.join(cypherT)

key = keyExtend(key,message)
message = encrypt(key,message)

server.listen()
print("\nSending Message...")
conn, addr = server.accept()
conn.send(str(message).encode(format))
print(f"Encryted Message Sent to [{addr}].")
conn.close()
server.close()
