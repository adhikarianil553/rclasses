
package com.mycompany.test_project;
import java.util.Scanner;
public class NewClass1 {
    public static void main(String args[])
    {
        Scanner sc = new Scanner (System.in);
        System.out.print ("Enter a number between 0-1000: ");
        int a = sc.nextInt();
        int sum = 0;
        while(a>0){
            sum += a%10;
            a /= 10;
        }
        System.out.println ("The sum is "+sum);
    }
}
