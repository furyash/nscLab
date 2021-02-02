import socket

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
message = conn.recv(size)   ###
print("Message Recieved:", message.decode(format))
conn.send(message)  ###
print('Message Reflected back.')
conn.close()               
server.close()