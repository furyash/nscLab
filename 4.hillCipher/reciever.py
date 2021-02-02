import socket

port = 4545
format = 'utf-8'
size  = 1024
client = socket.socket()
host = socket.gethostname()

client.connect((host,port))
message = client.recv(size).decode(format)
print(f"Encrypted Message recieved : {message}")

key = input('Enter the key : ').lower()

message = [ord(x)-97 for x in message]
key = [ord(x)-97 for x in key]
key = [key[:3],key[3:6],key[6:9]]

def determinant(key):
    """
    Finding determinant of (3x3) matrix 'key'
    """
    a = key[0][0]*(key[1][1]*key[2][2] - key[2][1]*key[1][2])
    b = key[0][1]*(key[1][0]*key[2][2] - key[2][0]*key[1][2])
    c = key[0][2]*(key[1][0]*key[2][1] - key[2][0]*key[1][1])
    return a - b + c

def modulo_inverse(det):
    """
    Finding Moudlo Inverse from the determinant 'det' of 26
    """
    det = det % 26;
    print(det) 
    for x in range(1, 26) : 
        if ((det * x) % 26 == 1) : 
            return x
    return 1

def inverse(key):
    """
    Inverse Matrix(3x3) of 'key' by Modulus 26
    """
    inv = modulo_inverse(determinant(key))
    adj11 = (key[1][1]*key[2][2] - key[2][1]*key[1][2]) * inv % 26
    adj12 = -(key[1][0]*key[2][2] - key[2][0]*key[1][2]) * inv % 26
    adj13 = (key[1][0]*key[2][1] - key[2][0]*key[1][1]) * inv % 26
    
    adj21 = -(key[0][1]*key[2][2] - key[2][1]*key[0][2]) * inv % 26
    adj22 = (key[0][0]*key[2][2] - key[2][0]*key[0][2]) * inv % 26
    adj23 = -(key[0][0]*key[2][1] - key[2][0]*key[0][1]) * inv % 26
    
    adj31 = (key[0][1]*key[1][2] - key[1][1]*key[0][2]) * inv % 26
    adj32 = -(key[0][0]*key[1][2] - key[1][0]*key[0][2]) * inv % 26
    adj33 = (key[0][0]*key[1][1] - key[1][0]*key[0][1]) * inv % 26
    
    return [[adj11,adj21,adj31],[adj12,adj22,adj32],[adj13,adj23,adj33]]
    
def decrypt(message,key):
    tex = ''
    for i in range(0,len(message)-1,3):
        tex+=(shrt_crypt(message[i:i+3],key))
    return tex

def shrt_crypt(mesg,key):
    a = chr(97+(key[0][0] * mesg[0] + key[0][1] * mesg[1] + key[0][2] * mesg[2]) % 26)
    b = chr(97+(key[1][0] * mesg[0] + key[1][1] * mesg[1] + key[1][2] * mesg[2]) % 26)
    c = chr(97+(key[2][0] * mesg[0] + key[2][1] * mesg[1] + key[2][2] * mesg[2]) % 26)
    return ''.join([a,b,c])

message = decrypt(message,inverse(key))
print("Decrypted Message : ",message)

client.close()

# NOTE : Although encryption algorithm works for any combination of keys, only limited keys work with
#        the decryption alorithm. As decryption algorithm utilizes modular multiplicative inverse on
#        determinant to find the KEY INVERSE matrix. Keys found working so far with both algorithms :
#        {alphabeta} {niniteman} {astalavista} {gybnqkurp} {ninyteman}