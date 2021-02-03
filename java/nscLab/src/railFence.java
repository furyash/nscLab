import java.util.*;

public class railFence {
    
    static void encryption(String text){
        if(text.length()%2 == 1) text += 'x';
        char[] cipher = new char[text.length()];
        int mid = text.length()/2;
        for (int i = 0; i < mid; i++) {
            cipher[i]     = text.charAt(2*i);
            cipher[mid+i] = text.charAt(2*i+1);
        }
        System.out.println(cipher);
    }
    static void decryption(String cipher){
        char[] text = new char[cipher.length()];
        int mid = cipher.length()/2;
        for (int i = 0; i < mid; i++) {
            text[2*i]   = cipher.charAt(i);
            text[2*i+1] = cipher.charAt(mid+i);
        }
        System.out.println(text);
    }
    
    public static void main(String[] args) {
        System.out.println("1)Encryption 2)Decryption 3)Exit");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("Enter the message :");
        String message = sc.nextLine();
        if (n == 1) encryption(message);
        if (n == 2) decryption(message);  
    }
}
