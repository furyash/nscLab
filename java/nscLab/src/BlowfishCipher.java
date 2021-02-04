import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class BlowfishCipher
{
    private static final String key = "123";
    public static String encryption(String pass)
    {
        try{
            byte[] keyData = (key).getBytes();
            SecretKeySpec sks = new SecretKeySpec(keyData, "Blowfish");
            
            Cipher c = Cipher.getInstance("Blowfish");
            c.init(Cipher.ENCRYPT_MODE,sks);
            byte[] hasil = c.doFinal(pass.getBytes());
            return new String(Base64.getEncoder().encode(hasil));
        }
        catch(Exception e)
        {
            e.printStackTrace();
            return null;
        }
    }
    public static String decryption(String str)
    {
        try{
            byte[] keyData = (key).getBytes();
            SecretKeySpec sks = new SecretKeySpec(keyData,"Blowfish");
            Cipher c = Cipher.getInstance("Blowfish");
            c.init(Cipher.DECRYPT_MODE,sks);
            byte[] hasil = c.doFinal(Base64.getDecoder().decode(str));
            return new String(hasil);
        }
        catch(Exception e)
        {
            e.printStackTrace();
            return null;
        }
    }
    public static void main(String[] args)
    {
        System.out.println("The ciphered text is:"+encryption("Test123"));
        String out = encryption("Test123");

        System.out.println("The Deciphered text is:"+decryption(out));
    }
}