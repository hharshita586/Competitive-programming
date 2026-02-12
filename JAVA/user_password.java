import java.util.Scanner;
class LoginSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String username;
        int password = 12345, input;
        int i = 0;
        
        System.out.print("Enter username: ");
        username = sc.nextLine();
        
        while (i < 3) {
            System.out.print("Enter password: ");
            input = sc.nextInt();
            if (input == password) {
                System.out.println("Access Granted! Welcome " + username);
                return;
            }
            i++;
            System.out.println("Wrong password! Attempt: " + i);
        }
        System.out.println("U r blocked!");
    }
}

