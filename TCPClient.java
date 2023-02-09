import java.net.*;
import java.io.*;
public class TCPClient{
    public static void main(String args[]) throws Exception{
        Socket clientSock = new Socket("127.0.01",4000);
        System.out.println("Client up.Enter file name");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String fname = br.readLine();
        InputStream istream = clientSock.getInputStream();
        OutputStream ostream = clientSock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream,true);
        pwrite.println(fname);
        BufferedReader contentRead = new BufferedReader(new InputStreamReader(istream));
        String str;
        while ((str = contentRead.readLine()) != null)
            System.out.println(str);
        clientSock.close();
        br.close();
    }
}