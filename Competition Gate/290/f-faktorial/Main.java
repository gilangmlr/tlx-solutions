import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
  public static void main (String[] args)
  {
    Scanner in = new Scanner(System.in);

    long faktorial;
    int n;

    String tmp = in.nextLine();
    n = Integer.parseInt(tmp);

    faktorial = 1;
    for(int i=1; i<=n; i++)
    {
          faktorial *= i;
    }

    System.out.println(faktorial);
  }
}