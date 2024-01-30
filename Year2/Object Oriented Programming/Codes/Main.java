import java.util.Scanner;

class Vehicle {
    String brandName;
    String model;
    int year;

    // Constructor to initialize the vehicle details
    public Vehicle(String brandName, String model, int year) {
        this.brandName = brandName;
        this.model = model;
        this.year = year;
    }

    // Method to display vehicle details
    public void show() {
        System.out.println("Brand: " + brandName);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}

class AdditionalDetails extends Vehicle {
    String type;

    // Constructor to initialize additional details
    public AdditionalDetails(String brandName, String model, int year, String type) {
        super(brandName, model, year); // Call the superclass constructor
        this.type = type;
    }

    // Method to display additional details
    public void display() {
        super.show(); // Call the superclass show method to display basic details
        System.out.println("Type: " + type);
    }
}

public class Main  {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Brand Name:");
        String brandName = scanner.nextLine();

        System.out.println("Enter Model:");
        String model = scanner.nextLine();

        int year;
        while (true) {
            System.out.println("Enter Year:");
            if (scanner.hasNextInt()) {
                year = scanner.nextInt();
                break;
            } else {
                System.out.println("Invalid input. Please enter a valid year.");
                scanner.nextLine(); // Consume the invalid input
            }
        }
        scanner.nextLine(); // Consume the newline character

        System.out.println("Enter Type:");
        String type = scanner.nextLine();

        // Create an instance of AdditionalDetails
        AdditionalDetails vehicleDetails = new AdditionalDetails(brandName, model, year, type);

        // Display the vehicle details, including additional details
        vehicleDetails.display();
    }
}
