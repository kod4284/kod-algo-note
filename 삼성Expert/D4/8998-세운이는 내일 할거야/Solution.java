import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.io.FileInputStream;
import java.util.StringTokenizer;
class Solution {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("/Users/daewoongko/Algo/삼성Expert/ D4/8998-세운이는 내일 할거야/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            int n = Integer.parseInt(br.readLine());
            PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o2[1] - o1[1]);
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                pq.add(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
            }

            int temp = pq.element()[1];
            while (!pq.isEmpty()) {
                int[] tAndD = pq.remove();
                temp = Math.min(temp, tAndD[1]) - tAndD[0];
            }
            System.out.printf("#%d %d\n", tc, temp);
        }
    }
}
