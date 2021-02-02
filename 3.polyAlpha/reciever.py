import socket

port = 4545
format = 'utf-8'
size  = 1024
client = socket.socket()
host = socket.gethostname()

client.connect((host,port))
message = client.recv(size).decode(format)
print(f"Encrypted Message recieved : {message}")

key = input("Enter key to decrypt : ").lower()

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

def decrypt(key, message):
    cypherT = []
    alpha = [chr(n) for n in range(97,123)]
    for i in range(len(message)):
        a= key[i]
        b= message[i]
        c = chr(97+(((97-ord(a)) + (97-ord(b)))%26))
        cypherT.append(c)
    return ''.join(cypherT)

key = keyExtend(key,message)
message = decrypt(key,message)
print("Decrypted Message : ",message)

client.close()
