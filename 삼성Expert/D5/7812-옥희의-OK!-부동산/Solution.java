import java.util.Scanner;
import java.io.FileInputStream;
import java.util.ArrayList;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		System.setIn(new FileInputStream("/Users/daewoongko/Algo/삼성Expert/D5/7812-옥희의-OK!-부동산/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            System.out.println("#" + test_case + " " + solve(sc));
		}
	}
    public static int solve(Scanner sc) {
		int end = 0, sumv = 0, cnt = 0;
		int N = sc.nextInt();
		int M = sc.nextInt();
		ArrayList<Integer> arr = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			arr.add(sc.nextInt());
		}
		for (int start = 0; start < N; start++) {
			while (end < N && sumv < M) {
				sumv += arr.get(end);
				end++;
			}
			if (sumv == M) {
				cnt++;
			}
			sumv -= arr.get(start);
		}
        return cnt;
    }
}