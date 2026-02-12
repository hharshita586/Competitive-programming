class Team
{
    public static void main(String[] ar)
    {
        String []arr={"Jay","Ram","Om","Sam", "Raj", "Anu","Dev", "Sam1", "Raj1", "Anu1","Dev1"};
        String sub="Amit";
        display(arr);
        check("Sam", arr);
        Replace("Sam", sub, arr);
    }

    public static void display(String ar[])
    {
        for(String o:ar)
            System.out.println(o);
    }

    public static void check(String s1, String s2[])
    {
        boolean found=false;
        for(String o:s2)
        {
            if(o.equals(s1))
            {
                found=true;
                break;
            }
        }
        if(found)
            System.out.println("Player exist in Team");
        else
            System.out.println("Player does not exist in Team");
    }

    public static void Replace(String s1, String sNew, String s2[])
    {
        for (int i=0; i<s2.length; i++)
        {
            if(s2[i].equals(s1))
                s2[i] = sNew;
            System.out.println(s2[i]);
        }
    }
}

