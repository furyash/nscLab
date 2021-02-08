
public class test {
    public static void main(String[] args) {
        
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
    }
}
