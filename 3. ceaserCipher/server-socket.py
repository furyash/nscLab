import socket

def decode(message):
    message = list(message)                #bytes(message.encode('ascii')))
    for i in range(len(message)):
        message[i] = chr(ord(message[i]) - key)
    return ''.join(message)

key = 3
format = 'utf-8'
size = 1024
port = 8585
server = socket.socket()         
host = socket.gethostname()                
server.bind((host, port))        

server.listen()                 
print('Listening...')

conn, addr = server.accept() ###    
print(f"[{addr}] Connected.")
message = conn.recv(size).decode(format)   ###
print("CypherText Recieved:", message)

print(f'Decrypted Message : {decode(message)}')

conn.close()               
server.close()