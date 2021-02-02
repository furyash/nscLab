import socket

def unstuff(message):
    i = 0
    new = ""
    c = 0
    while i < len(message):
        if message[i] == '1':
            c += 1
        else:
            c = 0
        new += message[i]
        i += 1
        if c == 5:
            i += 1
            c = 0
    return new

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
print("Message Recieved:", message)

print(f'Unstuffed Message : {unstuff(message)}')

conn.close()               
server.close()