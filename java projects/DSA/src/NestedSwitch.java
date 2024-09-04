import java.util.Scanner;

public class NestedSwitch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int emID = sc.nextInt();
        String department = sc.next();

        switch ((emID)) {
            case 1 -> System.out.println("pranesh");
            case 2 -> {
                switch (department) {
                    case "IT" -> System.out.println("IT department");
                    case "managemnet" -> System.out.println("management");
                }
            }
        }
        }
}
