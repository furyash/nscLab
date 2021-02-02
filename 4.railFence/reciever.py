import socket

port = 4545
format = 'utf-8'
size  = 1024
client = socket.socket()
host = socket.gethostname()

client.connect((host,port))
message = client.recv(size).decode(format)

print(f"Encrypted Message recieved : {message}")
key = int(input("Enter the key :"))

width = len(message)

tb =[[] for x in range(len(message)//key)]
for i in range(len(message)//key):
    for j in range(key):
        
        tb[i].append(message[i + j*(len(message)//key)])
        pass
tex = ''.join([y for x in tb for y in x])

print("Decrypted Message : ",tex)

client.close()
