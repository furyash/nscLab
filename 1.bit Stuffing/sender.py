import socket               

def bitstuff(message):
    data = list(message)
    i=0 
    c=0
    
    while(i<len(data)):
        if(data[i]=='1'):
            c+=1
        else: c=0

        if(c==6):
          data.insert(i,'0')
          c=0
        i+=1
    
    return ''.join(data)

format = 'utf-8'
size = 1024
port = 8585    
message = input('Enter binary message :')
client = socket.socket()          
host = socket.gethostname()
client.connect((host, port))

message = bitstuff(message)

client.send(message.encode(format))
print('Message sent to server.')
client.close()