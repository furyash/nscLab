import java.util.*;
class otp{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter key: ");
    String key = sc.next().toLowerCase();
    System.out.println("enter plaintext: ");
    String pt = sc.next();
    String ct = new String();
    for(int i=0;i<pt.length();i++)
    {
        int r = pt.charAt(i)-97;
        int c = key.charAt(i)-97;
        ct += (char)(((r+c)%26)+97);
    }
    System.out.println("ciphertext after encryption: "+ct);
    String msg = new String();
    for(int i=0;i<ct.length();i++)
    {
      int r = ct.charAt(i)-97;
      int c = key.charAt(i)-97;
      msg += (char)(((26+r-c)%26)+97);
    }
    System.out.println("Message after decryption: "+msg);
  }
}
