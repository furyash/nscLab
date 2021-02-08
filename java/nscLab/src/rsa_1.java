import java.util.Scanner;

public class rsa {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		long msg = in.nextLong();
		System.out.println("message: "+msg);
		System.out.println("enter 2 prime numbers: ");
		long p = in.nextLong();
		long q = in.nextLong();
		
		long n = p*q,phin = (p-1)*(q-1);
		long e=2;
		
		while(e<phin){
			if(gcd(e,phin)==1){
				break;
			}
			e+=1;
		}
		
		System.out.println("public key n = "+n+" e = "+e);
		
//		private key d => ed = 1 mod (p-1) (q-1)
		long d = 1;
		while(d<phin){
			if((d*e)%phin==1){
				break;
			}
			d+=1;
		}
		
		System.out.println("private key d = "+d);
		
		long cipher = powMod(msg,e,n);
		System.out.println("cipher text: "+(int)cipher);
		long plain = powMod(cipher,d,n);
		System.out.println("plain text: "+(int)plain);
		
	}
	
	static long gcd(long a,long b){
		if(b==0)
			return a;
		return gcd(b,a%b);
	}
	
	static long powMod(long a,long b,long m){
		long ans = 1;
		for(long i=0;i<b;i++){
			ans=((ans%m)*(a%m))%m;
		}
		return ans;
	}

}

