import java.util.*;

public class playfair {
    
    static void encrypt(String matrix[], int pos[][], int length){
        String cipher = "";
        for (int i = 0; i < length -1; i += 2) {
            
            if(pos[i][0] == pos[i+1][0]){
                cipher += matrix[pos[i][0]].charAt((pos[i][1] +1) %5);
                cipher += matrix[pos[i][0]].charAt((pos[i+1][1] +1) %5);
            }
            else if (pos[i][1] == pos[i+1][1]){
                cipher += matrix[(pos[i][0] +1) %5].charAt(pos[i][1]);
                cipher += matrix[(pos[i+1][0] +1) %5].charAt(pos[i][1]);
            }
            else{
                cipher += matrix[pos[i][0]].charAt(pos[i+1][1]);
                cipher += matrix[pos[i+1][0]].charAt(pos[i][1]);
            }
        }
        System.out.println("Encrypted Message :\n"+ cipher);
    }
    
    static void decrypt(String matrix[], int pos[][], int length){
        String text = "";
        for (int i = 0; i < length -1; i += 2) {
            
            if(pos[i][0] == pos[i+1][0]){
                text += matrix[pos[i][0]].charAt((pos[i][1] -1) %5);
                text += matrix[pos[i][0]].charAt((pos[i+1][1] -1) %5);
            }
            else if (pos[i][1] == pos[i+1][1]){
                text += matrix[(pos[i][0] -1) %5].charAt(pos[i][1]);
                text += matrix[(pos[i+1][0] -1) %5].charAt(pos[i][1]);
            }
            else{
                text += matrix[pos[i][0]].charAt(pos[i+1][1]);
                text += matrix[pos[i+1][0]].charAt(pos[i][1]);
            }
        }
        System.out.println("Original Message :\n"+ text);
    }

    static String inMatrix(String matrixArr, String arr){
        
        int i, j; boolean found = false;
        for (i = 0; i < arr.length(); i++) {
            found = false;
            for (j = 0; j < matrixArr.length(); j++) {
                if (matrixArr.charAt(j) == arr.charAt(i))
                    found = true;
            }
            if (found == false)
                matrixArr = matrixArr + arr.charAt(i);
        }
        return matrixArr;
    }
    
    public static void main(String[] args) throws Exception {
        String matrix[]={"","","","",""};
        String matrixArr = "", cipher="";
        int i = 0, j = 0, k = 0;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the message : ");
        String text = sc.nextLine();
        System.out.println("Enter the key : ");
        String key = sc.nextLine();
        
        int pos[][] = new int[text.length()][2];
        String alpha = "";
        for (i = 97; i < 122; i++) alpha += (char)i;
        
        matrixArr = matrixArr + key.charAt(0);
        matrixArr = inMatrix(matrixArr,key);
        matrixArr = inMatrix(matrixArr,alpha);

        for ( i = 0; i < 5; i++) 
            for ( j = 0; j < 5; j++) 
                matrix[i] = matrix[i] + matrixArr.charAt(k++);

        for ( i = 0; i < text.length(); i++) {
            for ( j = 0; j < 5; j++) {
                for ( k = 0; k < 5; k++) {
                    if (text.charAt(i) == matrix[j].charAt(k)){
                        pos[i][0] = j; pos[i][1] = k;
                    }
                }   
            }
        }
        System.out.println("1)Encryption 2) Decryption : ");
        int n = sc.nextInt();
        if (n == 1) encrypt(matrix, pos, text.length());
        if (n == 2) decrypt(matrix, pos, text.length());
        sc.close();
    }
}