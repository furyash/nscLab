import java.util.*;

public class oneTimePad {

    static char[] shuffleAlpha(char[] arr)
    {
        int n; char temp;
        Random rnd = new Random();
        for (int i = 0; i < 26; i++)
        {
            n = rnd.nextInt(i+1);
            temp = arr[n];
            arr[n] = arr[i];
            arr[i] = temp;
        }
        return arr;
    }

    static void encryption(){
        int i,ch;
        String text, cipher = "", keyOut="";
        char[] alpha, keyChar;
        alpha = keyChar = new char[26];
        for (i = 97; i < 123; i++) alpha[i-97] = (char)i;
        keyChar = shuffleAlpha(alpha);
        String key = new String(keyChar);

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a message :");
        text = sc.nextLine();
        System.out.println("Generated Key : ");
        for (i = 0; i < text.length(); i++){
            keyOut += (char)(key.indexOf(text.charAt(i))+ 97);
        }
        System.out.println(keyOut);
        for (i = 0; i < text.length(); i++) {
            ch = text.charAt(i);
            cipher += (char)((ch-97 + key.indexOf(text.charAt(i)))% 26 + 97);
        }
        System.out.println("Ciphertext :\n"+cipher);
        sc.close();
    }

    static void decryption(){
        int i,ch;
        String key="",cipher="",text="";

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the ciphertext :");
        cipher = sc.nextLine();
        System.out.println("Enter the key :");
        key = sc.nextLine();

        for (i = 0; i < cipher.length(); i++) {
            ch = cipher.charAt(i);
            ch -= ((int)key.charAt(i));
            if ( ch < 0) ch = ch + 26;
            text += (char)(ch+97);
            
        }
        System.out.println("Original Text :\n"+text);
        sc.close();
    }

    public static void main(String[] args){
        System.out.println("1)Encryption 2)Decryption 3)Exit");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n == 1) encryption();
        if (n == 2) decryption();    
    }
}