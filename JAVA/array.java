import java.util.Scanner;
public class array{
    public static void main(String []ar){
        int []a={8,6,7,5,4,2,3,1};
        int b[]= new int[5];
        Scanner sc=new Scanner(System.in);
        for(int i=0; i<b.length; i++)
        b[i]=sc.nextInt();
        System.out.println ("Enter the no. you want to search");
        int item;
        item=sc.nextInt();
        for(int i=0;i<a.length;i++)
        {
            if(a[i]==item){
                System.out.println("Element found on position="+(i+1));
                break;
            }
            
        }
    }
}