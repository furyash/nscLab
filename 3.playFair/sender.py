import socket

## Play Fair Matrix Calculation=====================================================================
def in_matrix(matrix,string):
    for j in range(len(string)):
        found = False
        for i in range(len(matrix)):
            if string[j] == matrix[i]:
                found = True
                break
        if found == False: 
            matrix.append(string[j])
    return matrix

def playfairMatrix(matrix,key,alpha):    
    matrix = in_matrix(matrix,key)
    matrix = in_matrix(matrix,alpha)

    matrix = [matrix[:5],matrix[5:10],matrix[10:15],matrix[15:20],matrix[20:]]
    print("\nPlayfair Matrix :")
    for row in matrix:
        print(row)
    return matrix


## Formatting Input ==================================================================================
def formatting(text):
    text = text.lower()
    text_format = []
    for i in range(len(text)):
        char=text[i]
        if i+1 > len(text_format) and i!=0:    #removing double letters and placing 'x' as filler
            if text[i] == text[i-1] and len(text_format)%2==1 :
                text_format.append('x')

        if char=='z':  #Replacing all 'z's in message with 'y'
            char ='y'
        text_format.append(char)
    if len(text_format)%2 != 0 :
        text_format.append('x')
    text = ''.join(text_format)
    print(f"Formatted message : {text}")
    return text


def encrypt(text,matrix):
    ## Calculating Positions of Input Message in Matrix =====================================================
    pos=[]
    for i in range(len(text)):
        for j in range(5):
            for k in range(5):
                if matrix[j][k] == text[i]:
                    pos.append((j,k))


    ## Mapping relative positions in Matrix ================================================================
    cipherT = []
    for i in range(0,len(text)-1,2):
        
        if pos[i][0] == pos[i+1][0]:
            cipherT.append(matrix[(pos[i][0])][(pos[i][1] + 1)%5])
            cipherT.append(matrix[(pos[i][0])][(pos[i+1][1] + 1)%5])
        elif pos[i][1] == pos[i+1][1]:
            cipherT.append(matrix[(pos[i][0] + 1)%5][(pos[i][1])])
            cipherT.append(matrix[(pos[i+1][0] + 1)%5][(pos[i][1])])
        else:
            cipherT.append(matrix[pos[i][0]][pos[i+1][1]])
            cipherT.append(matrix[pos[i+1][0]][pos[i][1]])
        #i=i+1

    print("Encrypted Message : ",''.join(cipherT))
    return ''.join(cipherT)


port = 4545
format = 'utf-8'
size  = 1024
server = socket.socket()
host = socket.gethostname()
server.bind((host,port))

key = input("Provide a KEY for Playfair Matrix : ")
key = key.lower()
alpha = [chr(n) for n in range(97,122)]  #chr(123)= z, used in matrix with y as 'y/z'
matrix = [key[0]]
matrix = playfairMatrix(matrix,key,alpha)

message = input("\nEnter message : ").replace(' ','')
message = formatting(message)
message = encrypt(message,matrix)

server.listen()
print("\nSending Message...")
conn, addr = server.accept()
conn.send(str(message).encode(format))
print(f"Encryted Message Sent to [{addr}].")
conn.close()
server.close()




