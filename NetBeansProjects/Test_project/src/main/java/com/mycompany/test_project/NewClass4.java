
package com.mycompany.test_project;
import java.util.Scanner;
public class NewClass4 {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your age");
        int age=sc.nextInt();
        System.out.println("voters age check");
        if(age>=18)
        {
            System.out.println("You are eligible for vote");
        }
        else
        {
            System.out.println("You are not eligible for vote");
        }
        
        
    }
}
