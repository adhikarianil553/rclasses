package com.mycompany.test_project;
import java.util.Scanner;

public class Test_project {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Calculation for the Area of the Circle");
        System.out.println("Enter the radius of Circle");
        int r = sc.nextInt();
        System.out.println("Enter the length of the Cylinder");
        int l = sc.nextInt();
        float A = (float)(r * r * 3.14);
        float V = (float)(A*l);
        System.out.println("The area of circle is:"+A);
         System.out.println("The volume of the cylinder is:"+V);
    }
}
