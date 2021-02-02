import socket

port = 4545
format = 'utf-8'
size  = 1024
client = socket.socket()
host = socket.gethostname()

client.connect((host,port))
message = client.recv(size).decode(format)

print(f"Encrypted Message recieved : {message}")
key = input("Enter key to decrypt : ")
print("\nDecrypting...")


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

def decrypt(cipherTex,matrix):
    ## Calculating Positions of Input Message in Matrix =====================================================
    pos=[]
    for i in range(len(cipherTex)):
        for j in range(5):
            for k in range(5):
                if matrix[j][k] == cipherTex[i]:
                    pos.append((j,k))

    ## Mapping relative positions in Matrix ================================================================
    tex = []
    for i in range(0,len(cipherTex)-1,2):
        
        if pos[i][0] == pos[i+1][0]:
            tex.append(matrix[(pos[i][0])][(pos[i][1] - 1)%5])
            tex.append(matrix[(pos[i][0])][(pos[i+1][1] - 1)%5])
        elif pos[i][1] == pos[i+1][1]:
            tex.append(matrix[(pos[i][0] - 1)%5][(pos[i][1])])
            tex.append(matrix[(pos[i+1][0] - 1)%5][(pos[i][1])])
        else:
            tex.append(matrix[pos[i][0]][pos[i+1][1]])
            tex.append(matrix[pos[i+1][0]][pos[i][1]])
        #i=i+1

    print("Decrypted Message : ",''.join(tex))
    return tex


## Formatting Output ==================================================================================
def formatting(text):
    text = text.lower()
    text_format = []
    for i in range(len(text)):
        char=text[i]
        if i>2:                             #removing filler 'x' letters
            if text[i] == text[i-2] and text[i-1]=='x' and len(text_format)%2==0 :
                text_format.pop()
        text_format.append(char)

    if len(text)%2 == 0 and text[len(text)-1]=='x' :
        text_format.pop()
    text = [str for str in text_format if str.isalpha()]
    print(f"Formatted/Original message : {''.join(text)}")

alpha = [chr(n) for n in range(97,122)]
matrix = [key[0]]

matrix = playfairMatrix(matrix,key,alpha)
message = decrypt(message,matrix)
message=formatting(str(message))

client.close()