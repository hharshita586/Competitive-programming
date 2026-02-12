import java.util.Scanner;

public class Student_class {
    int studentId;
    String name;
    int[] marks = new int[5];
    double avg;
    String grade;

    void input(int id, String n, int[] m) {
        studentId = id;
        name = n;
        marks = m;
        int sum = 0;
        for(int i = 0; i < 5; i++) sum += marks[i];
        avg = sum / 5.0;
        if(avg <= 50) grade = "C";
        else if(avg <= 60) grade = "B";
        else if(avg <= 70) grade = "B+";
        else if(avg <= 80) grade = "A";
        else if(avg <= 90) grade = "A+";
        else grade = "O";
        
    }
