class Student {
    int rollno;
    String name;
    int age;
    char grade;
    void setdata(int n, String s, int g, char d) {
        rollno = n;
        name = s;
        age = g;
        grade = d;
    }

    void display() {
        System.out.println("Roll no = " + rollno);
        System.out.println("Name = " + name);
        System.out.println("Age = " + age);
        System.out.println("Grade = " + grade);
    }

    public static void main(String[] ar) {
        Student s1 = new Student();
        s1.setdata(26, "Harshita", 20, 'A');
        s1.display();
    }
}
