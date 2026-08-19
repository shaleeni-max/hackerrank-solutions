import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
        
        int result=a;
            int term=b;
        for(int j=1;j<=n;j++){
            result=result+term;
            System.out.print(result+" ");
            term=term*2;
            
        }
        System.out.println();
        }
    
        
        
        in.close();
    }
}
