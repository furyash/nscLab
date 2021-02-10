import java.util.Scanner;
public class onetime {
  public static void main(String args[]) {
    
    Scanner s = new Scanner(System. in );
    System.out.println("Enter palin text to encrypt");
    String p = s.nextLine().toLowerCase();
    System.out.println("enter key");
    String key = s.nextLine();
    
    //Encryption
    String ci = "";
    for (int i = 0; i < p.length(); i++) {
      char c = p.charAt(i), k = key.charAt(i);
      
        ci += (char)((((c - 97) + (k - 97)) % 26) + 97);
    }
    System.out.println("cipher text is:" + ci);

    //Decryption
    p = "";
    for (int i = 0; i < ci.length(); i++) {
      char c1 = ci.charAt(i),k = key.charAt(i);
      p += (char)((((c1 - 97) - ( k - 97)  + 26) % 26) + 97);
    }

    System.out.println("plain text after decryption is:" + p);

  }
}