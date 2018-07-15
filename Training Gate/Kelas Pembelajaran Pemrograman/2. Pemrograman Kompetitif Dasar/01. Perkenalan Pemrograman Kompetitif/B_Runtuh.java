import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class B_Runtuh {
    public static void main(String[] args) {
        String[] line = U.rls(" ");
        int r = U.stoi(line[0]);
        int c = U.stoi(line[1]);

        int[][] mat = new int[r][c];
        for (int i = 0; i < r; i++) {
            line = U.rls("");
            for (int j = 0; j < line.length; j++) {
                mat[i][j] = U.stoi(line[j]);
            }
        }
        U.wl(U.artos(mat));
    }

    public static void runtuh(int[][] ar) {
        boolean anyFull = false;
        int lrow = 0;
        for (int i = 0; i < ar.length; i++) {
            boolean full = true;
            for (int j = 0; j < ar[0].length; j++) {
                if (ar[i][j] == 0) {
                    full = false;
                }
            }
            if (full) {
                anyFull = true;
                lrow = i;
                for (int j = 0; j < ar[0].length; j++) {
                    ar[i][j] = 0;
                }
            }
        }
        if (!anyFull) {
            return;
        }
        for (int j = 0; j < ar[0].length; j++) {
            int nlrow = lrow;
            for (int i = lrow; i < ar.length; i++) {
                if (ar[i][j] == 0) {
                    nlrow = i;
                }
            }
            int[] nrow = new int[nlrow + 1];
            for (int i = 0; i <= nlrow; i++) {
                nrow[i] = ar[i][j];
            }
            Arrays.sort(nrow);
            for (int i = 0; i <= nlrow; i++) {
                ar[i][j] = nrow[i];
            }
        }

        runtuh(ar);
    }
}

class U {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void wl(String message) {
        try {
            bw.write(message + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String[] rls(String delim) {
        return rl().split(delim);
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

