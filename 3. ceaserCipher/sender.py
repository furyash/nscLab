import socket               

def encode(message):
    message = list(message)                #bytes(message.encode('ascii')))
    for i in range(len(message)):
        message[i] = chr(ord(message[i]) + key)
    return ''.join(message)
    
key = 3 #Encrytion Key
format = 'utf-8'
size = 1024
port = 8585    
message = input('Enter message :')
client = socket.socket()          
host = socket.gethostname()
client.connect((host, port))

message = encode(message)

client.send(message.encode(format))
print('Encrypted Message sent to server.')
client.close()