import socket

port = 4545
format = 'utf-8'
size  = 1024
client = socket.socket()
host = socket.gethostname()

client.connect((host,port))
message = client.recv(size).decode(format)
key = client.recv(size).decode(format)

print(f"Encrypted Message recieved : {message}")
print("Key recieved : ",key)


def decrypt(key, message):
    tex = []
    #alpha = [chr(n) for n in range(97,123)]
    for i in range(len(message)):
        c = chr(97+key.index(message[i]))
        tex.append(c)
    return ''.join(tex)

message = decrypt(key,message)
print("Decrypted Message : ",message)

client.close()
