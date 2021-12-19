import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Map;
import java.util.HashMap;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

class TrieNode {
	private Map<Character, TrieNode> childNodes = new HashMap<>();
	private int count;

	TrieNode() {
		this.count = 1;
	}

	Map<Character, TrieNode> getChildNodes() {
		return this.childNodes;
	}

	int getCount() {
		return this.count;
	}

	void upCount() {
		this.count += 1;
	}
}

class UserSolution {
	private TrieNode root;
	
	public void init() {	
		this.root = new TrieNode();
	}
	
	public void insert(int buffer_size, String buf) {	
		TrieNode node = this.root;
		for (int i = 0; i < buffer_size; i++) {
			Character c = buf.charAt(i);
			TrieNode nextNode = node.getChildNodes().get(c);
			if (nextNode != null) {
				nextNode.upCount();
				node = nextNode;
			} else {
				node = node.getChildNodes().computeIfAbsent(c, t -> new TrieNode());
			}
		}
	}
	
	public int query(int buffer_size, String buf) {
		TrieNode node = this.root;
		for (int i = 0; i < buffer_size; i++) {
			node = node.getChildNodes().get(buf.charAt(i));
			if (node == null) {
				return 0;
			}
		}
		return node.getCount();
	}
}
public class Solution {
    
	public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("/Users/daewoongko/Algo/삼성Expert/D5/3135-홍준이의-사전놀이/input.txt"));
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);

		UserSolution dictManager = new UserSolution();
		
		for (int TestCase = in.nextInt(), tc = 1; tc <= TestCase; tc = tc + 1) {

			int Query_N = in.nextInt();

			out.print("#" + tc);

			dictManager.init();

			for (int i = 1; i <= Query_N; i++) {
				int type = in.nextInt();

				if (type == 1) {
					String buf = in.next();
					dictManager.insert(buf.length(), buf);
				}
				else {
					String buf = in.next();
					int answer = dictManager.query(buf.length(), buf);
					out.print(" " + answer);
				}
			}
			out.println("");
		}
		out.close();
	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
			tokenizer = null;
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				}
				catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

	}
}
