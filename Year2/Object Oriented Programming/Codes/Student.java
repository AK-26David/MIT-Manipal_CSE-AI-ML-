import java.util.Scanner;
class student
{
    int regno;
    String name;
    int age;
    student(String name,int regno,int age)
    {
        this.regno=regno;
        this.name=name;
        this.age=age;
    }
    void display()
    {
        System.out.print("Name of the student:"+name);
        System.out.print("Registration Number:"+regno);
        System.out.print("Age:"+age);
    }
}
class UG extends student
{
    int semester;
    int fees;
    UG(String name,int regno,int age,int semester,int fees)
    {
        super(name,regno,age);
        this.semester=semester;
        this.fees=fees;
    }
    void displayUG()
    {
        System.out.print("Semester:"+semester);
        System.out.print("Fees paid by student:"+fees);
    }
}
class main
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the name of the student:");
        String name=sc.nextLine();
        System.out.print("Enter the registration number of the student:");
        int regno=sc.nextInt();
        System.out.print("Enter the age of the student:");
        int age=sc.nextInt();
        System.out.print("Enter the semester of the student:");
        int semester=sc.nextInt();
        System.out.print("Enter the fees paid by the student:");
        int fees=sc.nextInt();
        UG ugstudents=new UG(name,regno,age,semester,fees);
        ugstudents.display();
        ugstudents.displayUG();
        sc.close();
    }
}