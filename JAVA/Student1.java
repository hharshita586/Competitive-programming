class student1
{
    int r ;
    String nm;
    student1(int r,String nm)
    {
        this.r=r;
        this.nm=nm;
    }
    void display()
    {
        System.out.println("Roll no: "+r);
        System.out.println("Name: "+nm);
    }
    public static void main(String args[])
    {
        student1 s1=new student1(26,"Harshita");
        s1.display();
    }
}
