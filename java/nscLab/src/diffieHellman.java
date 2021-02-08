import java.util.HashSet;
import java.util.Scanner;

public class diffieHellman {
    public static void main(String []args){

        Scanner sc = new Scanner(System.in);
        long q,a=-1;
        System.out.println("Select a prime number");
        q = sc.nextLong();

//        get primitive root of q
        long temp = 1;
        for(long k=1;k<q;k++) {
            a = k;
            HashSet<Long> s = new HashSet<>();
            boolean primitiveRoot = true;
            for (long i = 1; i < q; i++) {
                temp *= k;
                temp%=q;
                if (s.contains(temp)) {
                    primitiveRoot = false;
                    break;
                } else {
                    s.add(temp);
                }
                System.out.println(s);
            }
            if(primitiveRoot==true){
                break;
            }
        }

        System.out.println("Public numbers q="+q+" a="+a);

//        private keys
        System.out.println("Private key Xa and Xb");

        long Xa=sc.nextLong(),Xb=sc.nextLong();

//        public keys
        long Ya,Yb;
        Ya = (long)Math.pow(a,Xa);
        Yb = (long)Math.pow(a,Xb);

        long k1,k2;
        
        k1 = modPow(Yb,Xa,q);
        k2 = modPow(Ya,Xb,q);

        System.out.println("Secret keys calculated by A and B");
        System.out.println(k1+" == "+k2);


    }

    static long modPow(long a, long b,long mod){
        long ans = 1;
        for(long x=0;x<b;x++){
            ans = (ans*a)%mod;
        }
        return ans;
    }


}
