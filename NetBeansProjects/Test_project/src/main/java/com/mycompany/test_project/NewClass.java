package com.mycompany.test_project;
import java.util.Scanner;

public class NewClass {
    public static void main(String arg[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("fhareheit to celcius") ;
        System.out.println("Enter temp in fhareheit");
        float fharen = sc.nextFloat();
        float celcius = (fharen-32)*5/9;
        System.out.println("The temp in celcius is: "+celcius);
        
    }
}
