import socket               

format = 'utf-8'
size = 1024
port = 8585    
message = input('Enter message to send : ')
client = socket.socket()          
host = socket.gethostname()

client.connect((host, port))
client.send(message.encode(format))
print('Message sent to server.')
print("Message Recieved:", client.recv(size).decode(format))
client.close()