import socket               

def charcountstuff(message):
    data = list(message)
    i=0 
    c=0

    while (i<len(data)):
        if c == frameSize-1:
            data.insert(i-frameSize,frameSize)
            i+=1
        else: 
            if data[i+1]=='' :
                data.insert((i-(i+1)%frameSize),(i+1)%frameSize)
        i+=1
  
    return ''.join(data)

frameSize = 4
format = 'utf-8'
size = 1024
port = 8585    
message = input('Enter message :')
client = socket.socket()          
host = socket.gethostname()
client.connect((host, port))

message = charcountstuff(message)

client.send(message.encode(format))
print('Message sent to server.')
client.close()