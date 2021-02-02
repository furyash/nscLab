import socket

port = 4545
format = 'utf-8'
size  = 1024
client = socket.socket()
host = socket.gethostname()

client.connect((host,port))
message = client.recv(size).decode(format)
print(f"Encrypted Message recieved : {message}")

key = input("Enter the key :")
sKey = sorted(key)

leng = len(key)
width = len(message)

tb =[[] for x in range(width//leng)]

for i in range(width//leng):
    
    for j in range(leng):
        #print(sKey.index(key[j]),end=',')        
        tb[i].append(message[(sKey.index(key[j]))*(width//leng)+i])
        pass
tex = ''.join([y for x in tb for y in x])

print("Decrypted Message : ",tex)


client.close()

