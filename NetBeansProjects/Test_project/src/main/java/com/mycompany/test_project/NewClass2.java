
package com.mycompany.test_project;
import java.util.Scanner;
public class NewClass2 {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System. in);
        System.out.println("Enter some letter");       
        String text = sc.next();
        String lower = text.toLowerCase();
        System.out.println(lower);
    }
}
