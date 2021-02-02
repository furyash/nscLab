import socket

def unstuff(message):
    # Using Dilimiter : 'D'
    # Escape Character: 'X'
    i = 0
    new = ""
    
    while i < len(message):
        if message[i] == 'D' and (i == 0 or i == len(message)-1):
            i += 1
            continue

        if message[i] == 'X' and message[i+1] == 'X':
            i += 1

        if message[i] == 'X' and message[i+1] == 'D':
            i += 1

        new += message[i]
        i += 1
    return new    

frameSize = 4
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