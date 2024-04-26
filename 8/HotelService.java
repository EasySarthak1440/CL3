import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelService extends Remote {
    boolean bookRoom(int roomNumber, String guestName) throws RemoteException;
    boolean cancelBooking(int roomNumber) throws RemoteException;
}
