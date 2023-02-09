import java.net.*;
import java.io.*;
public class TCPServer{
    public static void main(String arg[]) throws Exception{
        ServerSocket connSock = new ServerSocket(4000);
        System.out.println("Waiting for client");
        Socket sock = connSock.accept();
        System.out.println("Connection estabilished ");
        InputStream istream = sock.getInputStream();
        String fname;
        BufferedReader newRead = new BufferedReader(new InputStreamReader(istream));
        fname = newRead.readLine();
        BufferedReader contentRead = new BufferedReader(new FileReader(fname));
        String str;
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream,true);
        while ((str = contentRead.readLine()) != null)
            pwrite.println(str);
        System.out.println("Closing");
        sock.close();
        connSock.close();
        newRead.close();
        contentRead.close();
    }
}