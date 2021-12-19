import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.io.FileInputStream;

public class Solution2 {
    public static void main(String[] args) throws NumberFormatException, IOException {
    System.setIn(new FileInputStream("/Users/daewoongko/Algo/삼성Expert/D4/8998-세운이는 내일 할거야/input.txt"));
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; tc++) {
            int n = Integer.parseInt(br.readLine());
            PriorityQueue<Schedule> pq = new PriorityQueue<>();
            StringTokenizer st;
            for(int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                pq.add(new Schedule(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())));
            }
            Schedule sch = pq.poll();
            long start_day = sch.day - sch.time + 1;
            while(!pq.isEmpty()) {
                Schedule schedule = pq.poll();
                long day = schedule.day;
                long st1 = day - schedule.time + 1;
                if(start_day <= day) {
                    start_day = st1 - (day - start_day + 1);
                }else {
                    start_day = st1;
                }
            }
            System.out.println("#" + tc + " " + (start_day - 1));
        }
    }
     
    public static class Schedule implements Comparable<Schedule> {
        int time, day;
            Schedule(int time, int day){
                this.time = time;
                this.day = day;
            }
            @Override
            public int compareTo(Schedule o) {
                return o.day < this.day ? -1 : 1;
            }
         
    }
}
