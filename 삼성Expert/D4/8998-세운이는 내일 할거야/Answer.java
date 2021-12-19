import java.util.*;
import java.io.*;

class Answer {
    private static int solve(BufferedReader br) throws Exception {
        int n = Integer.parseInt(br.readLine());
        ArrayList<int[]> arr = new ArrayList<int[]>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int[] temp = {t, d};
            arr.add(temp);
        }
        
        Collections.sort(arr, new Comparator<int[]>(){
            @Override
                public int compare(int[] o1, int[] o2) {
                    return o2[1] - o1[1];
                }
        });

        int min = 99999;
        for (int i = 0; i < n; i++) {
            int t = arr.get(i)[0];
            int d =arr.get(i)[1];
            if (i == 0) {
                min = d - t;
                continue;
            }
            min = Math.min(min, d) - t;
        }
        return min;
    }
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("/Users/daewoongko/Algo/삼성Expert/ D4/8998-세운이는 내일 할거야/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());

        for(int tc = 1; tc <= TC; tc++) {
            System.out.printf("#%d %d\n",tc, solve(br));
        }

    }
}