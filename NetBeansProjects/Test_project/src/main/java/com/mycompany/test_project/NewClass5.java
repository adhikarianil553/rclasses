
package com.mycompany.test_project;
import java.util.Scanner;
public class NewClass5 {
    public static void main(String args[])
    {Scanner sc=new Scanner(System. in);
    System.out.println("enter your age");
    int age=sc.nextInt();
    System.out.println("voters age check");
        if(age<18)
                {
                System.out.println("voters age doesnot match");
                }
        else if(age>=18 && age<70)
                {
                System.out.println("voters age  match");
                }
        else
                {
                System.out.println("voters age doesnot match");
                }
    
}
    
    
}
