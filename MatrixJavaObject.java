/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaapplication8;

import java.util.Scanner;
import java.util.Arrays;

/**
 *
 * @author aulamovil25
 */
public class JavaApplication8 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner leer = new Scanner(System.in);
        
        Object[][] Estudiantes = new Object[2][4];
        double suma = 0;
        double promedio = 0;
        
        for (int i=0; i<2; i++){
            for (int j=0; j<4; j++){
                if (i == 0){
                    System.out.println("Ingresa el estudiante " + (j+1));
                    Estudiantes[i][j] = leer.next();
                } else {
                    System.out.println("Ingresa la nota " + (j+1));
                    Estudiantes[i][j] = leer.nextDouble();
                    suma += (double)(Estudiantes[i][j]);
                }
                
            }
        }
        
        System.out.println("Los estudiantes ingresados con sus respectivas notas son:");
        
        for (int i=0; i<2; i++){
            for (int j=0; j<4; j++){
                System.out.print(Estudiantes[i][j] + " ");
            }
            System.out.println("");
        }
        
  
        promedio = suma / Estudiantes[0].length;
        
        System.out.println("El promedio de notas es: " + promedio);
    }
    
}
