import java.util.*;

public class ceaser {
    static void encryption(String text, int key){
        char c; String cipher="";
        for (int i = 0; i < text.length(); i++) {
            c = text.charAt(i);
            cipher += (char)((((c - 97) + key) % 26) + 97);
        }
        System.out.println("Ciphertext :\n" + cipher);
    }
    
    static void decryption(String cipher, int key){
        char c; String text="";
        for (int i = 0; i < cipher.length(); i++) {
            c = cipher.charAt(i);
            text += (char)((((c - 97) - key) % 26) + 97);
        }
        System.out.println("Original Text :\n" + text);
    }

    public static void main(String[] args){
        int key; String text="";
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the message :");
        text = sc.nextLine().toLowerCase();
        System.out.println("Enter the key :");
        key = sc.nextInt();

        System.out.println("1)Encryption 2)Decryption 3)Exit");
        int n = sc.nextInt();
        if (n == 1) encryption(text,key);
        if (n == 2) decryption(text,key);    
    }
}
