import java.util.Scanner;
public class PolyalphabeticCipher
{
    public static String encrypt(String text,String key)
    {
        String res = "";
        text = text.toUpperCase();
        for (int i = 0, j = 0; i < text.length(); i++)
        {
            char c = text.charAt(i);
            if (c < 'A' || c > 'Z')
                continue;
            res += (char) (((c-65) + (key.charAt(j)-65)) % 26 +65);
            j = ++j % key.length();
        }
        return res;
    }
 
    public static String decrypt(String text,String key)
    {
        String res = "";
        text = text.toUpperCase();
        for (int i = 0, j = 0; i < text.length(); i++)
        {
            char c = text.charAt(i);
            if (c < 'A' || c > 'Z')
                continue;
            res += (char) ((c - key.charAt(j) + 26) % 26 + 65);
            j = ++j % key.length();
        }
        return res;
    }
 
    public static void main(String[] args)
    {
		Scanner s=new Scanner(System.in);
		 
	   System.out.println("Enter text to encrypt:");
	   

        String message =s.nextLine(); 
 		 System.out.println("Enter key:");
		 String  key=s.nextLine();
        String encryptedMsg = encrypt(message, key);
        System.out.println("Encrypted message: " + encryptedMsg);
        System.out.println("Decrypted message: " + decrypt(encryptedMsg, key));
    }
}