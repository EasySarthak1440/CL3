import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer extends UnicastRemoteObject implements HotelService {
    private Map<Integer, String> bookings;

    protected HotelServer() throws RemoteException {
        bookings = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(int roomNumber, String guestName) throws RemoteException {
        if (!bookings.containsKey(roomNumber)) {
            bookings.put(roomNumber, guestName);
            System.out.println("Room " + roomNumber + " booked for " + guestName);
            return true;
        } else {
            System.out.println("Room " + roomNumber + " is already booked");
            return false;
        }
    }

    @Override
    public synchronized boolean cancelBooking(int roomNumber) throws RemoteException {
        if (bookings.containsKey(roomNumber)) {
            String guestName = bookings.remove(roomNumber);
            System.out.println("Booking for room " + roomNumber + " cancelled for guest " + guestName);
            return true;
        } else {
            System.out.println("No booking found for room " + roomNumber);
            return false;
        }
    }

    public static void main(String[] args) {
        try {
            HotelServer server = new HotelServer();
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            java.rmi.Naming.rebind("HotelService", server);
            System.out.println("Hotel server started.");
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
