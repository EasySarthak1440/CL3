import java.rmi.Naming;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelService hotelService = (HotelService) Naming.lookup("rmi://localhost/HotelService");

            // Book a room
            boolean booked = hotelService.bookRoom(101, "John Doe");
            if (booked) {
                System.out.println("Room booked successfully.");
            }

            // Cancel booking
            boolean cancelled = hotelService.cancelBooking(101);
            if (cancelled) {
                System.out.println("Booking cancelled successfully.");
            }
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
