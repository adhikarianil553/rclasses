
package com.mycompany.test_project;
import java.util.Scanner;
public class NewClass3 {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System. in);
        System.out.print("Enter you number to convert in ASCII:");
        int a= sc.nextInt();
        char ascii=(char) a;
        System.out.println("the number in Ascii is:"+ascii);
    }
    
}
