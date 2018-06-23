import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class A_SeleksiOlimpiade {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) {
        int t = Integer.parseInt(rl());
        for (int j = 0; j < t; j++) {
            String[] line = rl().split(" ");
            int n = Integer.parseInt(line[0]);
            int m = Integer.parseInt(line[1]);
            String targetId = rl();
            Participant[] ps = new Participant[n];
            for (int i = 0; i < n; i++) {
                line = rl().split(" ");
                Participant p = new Participant(line[0], Integer.parseInt(line[1]), Integer.parseInt(line[2]), Integer.parseInt(line[3]));
                ps[i] = p;
            }
            Arrays.sort(ps);
            boolean passed = false;
            for (int i = 0; i < m; i++) {
                if (ps[i].id.compareTo(targetId) == 0) {
                    passed = true;
                    break;
                }
            }
            if (passed) {
                wl("YA");
            } else {
                wl("TIDAK");
            }
        }
    }

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

    public static String ats(Object[] arr) {
        return Arrays.toString(arr);
    }

    public static String ats(int[] arr) {
        return Arrays.toString(arr);
    }

    public static String ats(float[] arr) {
        return Arrays.toString(arr);
    }
}

class Participant implements Comparable<Participant> {
    String id;
    int sesi1;
    int sesi2;
    int sesi3;

    public Participant(String id, int sesi1, int sesi2, int sesi3) {
        this.id = id;
        this.sesi1 = sesi1;
        this.sesi2 = sesi2;
        this.sesi3 = sesi3;
    }

    @Override
    public int compareTo(Participant p) {
        if (p.sesi3 - this.sesi3 != 0) {
            return p.sesi3 - this.sesi3;
        } else {
            if (p.sesi2 - this.sesi2 != 0) {
                return p.sesi2 - this.sesi2;
            } else {
                if (p.sesi1 - this.sesi1 != 0) {
                    return p.sesi1 - this.sesi1;
                } else {
                    return 0;
                }
            }
        }
    }

    @Override
    public String toString() {
        return "[" + this.id + ", " + this.sesi1 + ", "
            + this.sesi2 + ", " + this.sesi3 + "]";
    }
}
