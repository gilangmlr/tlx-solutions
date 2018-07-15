import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main {
    public static void main(String[] args) {
        int n = U.stoi(U.rl());
        if (n > 0) {
            U.wl("positif");
        } else if (n < 0) {
            U.wl("negatif");
        } else {
            U.wl("nol");
        }
    }
}

class U {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void wl(String message) {
        try {
            bw.write(message + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String rl() {
        try {
            return br.readLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "";
    }

    public static int stoi(String i) {
        return Integer.parseInt(i);
    }

    public static String artos(Object[] arr) {
        return Arrays.toString(arr);
    }

    public static String artos(int[] arr) {
        return Arrays.toString(arr);
    }

    public static String artos(float[] arr) {
        return Arrays.toString(arr);
    }
}