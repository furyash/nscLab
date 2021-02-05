package mlab;

import java.util.Scanner;

public class rsa {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int msg = in.nextInt();
		System.out.println("message: "+msg);
		System.out.println("enter 2 prime numbers: ");
		int p = in.nextInt();
		int q = in.nextInt();
		
		int n = p*q,phin = (p-1)*(q-1);
		int e=2;
		
		while(e<phin){
			if(gcd(e,phin)==1){
				break;
			}
			e+=1;
		}
		
		System.out.println("public key n = "+n+" e = "+e);
		
//		private key d => ed = 1 mod (p-1) (q-1)
		double d = 1;
		while(d<phin){
			if((d*e)%phin==1){
				break;
			}
			d+=1;
		}
		
		System.out.println("private key d = "+d);
		
		double cipher = (int)Math.pow(msg*1.0, e*1.0);
		cipher = cipher%n;
		System.out.println("cipher text: "+(int)cipher);
		double plain = Math.pow(cipher, d)%n;
		System.out.println("plain text: "+(int)plain);
		
	}
	
	static int gcd(int a,int b){
		if(b==0)
			return a;
		return gcd(b,a%b);
	}

}

