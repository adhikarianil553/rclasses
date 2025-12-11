/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.test_project;

import java.util.Scanner;
public class NewClass6 {
    public static void main(String[]args)
    {
        Scanner sc= new Scanner(System.in);
        for(int i=0;i<10;i++)
        {
            System.out.println("line no."+(i+1));
        }
        System.out.println("do you want to print line? y/n");
        char x= Scanner.next().charAt(0);
        do{
            System.out.println("line printed");
            System.out.println("do you want to print line more? y/n");
            x=sc.next().charAt(0);
        }while (x == 'y'|| x == 'y');
                sc.close();
                System.out.println ("exit the loop");

    }
    
}
