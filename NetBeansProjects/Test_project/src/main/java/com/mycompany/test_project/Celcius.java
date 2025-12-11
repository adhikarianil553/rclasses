package com.mycompany.test_project;
import java.util.Scanner;
public class Celcius {
    public static void main(String[] arg)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Conversion of Fharenhiet to Celcius");
        System.out.println("Enter temperature in Fharenhiet");
        float Fharenhiet = sc.nextFloat();
        float Celcius = (Fharenhiet-32)*5/9;
        System.out.println("The temperature in Celcius is: "+Celcius);
    }
   
}