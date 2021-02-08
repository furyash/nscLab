import java.math.BigInteger;
import java.util.Scanner;
public class RSA {
    static int gcd (int a,int b){
		if (b == 0) return a;
		return gcd(b, a % b);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger text, n, cipher;
        System.out.print("Enter a message : ");
        text = sc.nextBigInteger();
        System.out.println("Enter two prime numbers :");
        int x = sc.nextInt(); 
        int y = sc.nextInt();
        n = BigInteger.valueOf(x * y);
        int d = 0, e = 1;
        int phin = (x - 1) * (y - 1);
        while (e < phin)
            if (gcd(++e, phin) == 1)
                break;
        System.out.println("Public Key  : ("+e+", "+n+")");
        while (d < phin)
            if ((++d * e)% phin == 1)
                break;
        System.out.println("Private Key : ("+d+", "+n+")");
        
        cipher = text.pow(e).mod(n);
        System.out.println("Ciphertext  : "+ cipher);
        text = cipher.pow(d).mod(n);
        System.out.println("Plaintext   : "+ text);

    }
}
