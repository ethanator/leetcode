class Solution {
  public int numDecodings(String s) {
    int len = s.length();
    if (len == 0 || s.charAt(0) == '0') return 0;
    if (len == 1) return 1;
    
    int dp[] = new int[len + 1];
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 1; i < len; i++) {
      char c = s.charAt(i);
      char prev = s.charAt(i - 1);
      if (c == '0') {
        if (prev != '1' && prev != '2') return 0;
        dp[i + 1] = dp[i - 1];
        continue;
      }
      if (prev > '1' && c > '6') {
        dp[i + 1] = dp[i];
        continue;
      }
      if (prev == '1' || prev == '2') {
        dp[i + 1] = dp[i - 1] + dp[i];
      } else {
        dp[i + 1] = dp[i];
      }
    }

    return dp[len];
  }
}

public class DecodeWays {
  public static void main(String[] args) {
    System.out.println(new Solution().numDecodings("0"));
  }
}