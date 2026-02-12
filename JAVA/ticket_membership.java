import java.util.*;

class MovieTicketTotal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Children (<12): ");
        int n = sc.nextInt();
        System.out.print("Senior citizens (>=65): ");
        int m = sc.nextInt();
        System.out.print("Adults (12-64): ");
        int a = sc.nextInt();
        System.out.print("Membership? (true/false): ");
        boolean membership = sc.nextBoolean();

        int total = n * 5 + m * 7 + a * 10 - (membership ? 2 : 0);
        System.out.println("Total Ticket Price: $" + total);
    }
}
