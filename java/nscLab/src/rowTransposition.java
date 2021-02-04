import java.util.*;

public class rowTransposition {
    static void encryption(String text, String key, int x, int y){
        String cipher = ""; int i,j,k=0;
        char[] skey  = key.toCharArray();
        Arrays.sort(skey);
        
        char[][] table = new char[y][x]; 
        for (i = 0; i < y; i++) for (j = 0; j < x; j++)
                table[i][j] = text.charAt(k++);
        for (i = 0; i < x; i++) for (j = 0; j < y; j++)
                cipher += table[j][key.indexOf(skey[i])];
        System.out.println("CipherText : "+cipher);
    }
    static void decryption(String cipher, String key, int x, int y){
        String text = ""; int i,j,k=0;
        char[] skey =  key.toCharArray();
        Arrays.sort(skey); String ckey = new String(skey);

        char[][] table = new char[y][x]; 
        for (i = 0; i < x; i++) for (j = 0; j < y; j++)
                table[j][i] = cipher.charAt(k++);
        for (i = 0; i < y; i++) for (j = 0; j < x; j++)
                text += table[i][ckey.indexOf(key.charAt(j))];
        System.out.println("OriginalText : "+text);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the message :");
        String mesg = sc.nextLine();
        System.out.println("Enter the key :");
        String key  = sc.nextLine();

        int i, x = key.length();
        int y = mesg.length() % x;
        if (y != 0) for (i = 0; i < x-y; i++) mesg += 'x';
        y = mesg.length() / x;
        System.out.println("1)Encryption 2) Decryption : ");
        int n = sc.nextInt();
        if (n == 1) encryption(mesg, key, x, y);
        if (n == 2) decryption(mesg, key, x, y);
    }
}
