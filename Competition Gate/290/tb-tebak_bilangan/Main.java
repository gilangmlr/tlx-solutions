import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
  public static void main (String[] args) throws Exception
  {
    int[] data = new int[100005];

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int upper, lower, guess;
    int n, query, x;
    String tmp;
    String[] tmps;


    tmp = br.readLine();
    n = Integer.parseInt(tmp);

    tmps = br.readLine().split(" ");
    for(int i=0; i<n; i++)
    {
        data[i] = Integer.parseInt(tmps[i]);
    }

    tmp = br.readLine();
    query = Integer.parseInt(tmp);
    for(int i=0; i<query; i++)
    {
        tmp = br.readLine();
        x = Integer.parseInt(tmp);

        upper = n-1;
        lower = 0;

        guess = 0;
        int co = 0;
        while(upper != lower)
        {
            guess = (int) Math.ceil((upper + lower) / 2.0);

            if(data[guess] > x)
            {
                upper = guess;
            }
            else if(data[guess] < x)
            {
                lower = guess;
            }
            else
            {
                break;
            } co++;
            if (co > Math.log(n) + 5) {
                break;
            }
            
        }

        if(data[guess] == x)
        {
            System.out.println("Ada");
        }
        else
        {
            System.out.println("Tidak Ada");
        }
    }
  }
}