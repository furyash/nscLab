import socket               

def charstuff(message):
    # Using Dilimiter : 'D'
    # Escape Character: 'X'
    data = list(message)
    i=0 

    
    while (i<len(data)):
        if data[i]=='D' or data[i]=='X':
            data.insert(i,'X')
            i+=1
        i+=1
  
    new = ''.join(data)
    new = 'D' + new + 'D'
    return new

format = 'utf-8'
size = 1024
port = 8585    
message = input('Enter message :')
client = socket.socket()          
host = socket.gethostname()
client.connect((host, port))

message = charstuff(message)

client.send(message.encode(format))
print('Message sent to server.')
client.close()