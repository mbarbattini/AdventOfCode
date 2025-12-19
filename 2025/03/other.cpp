/*
  Top-down Iterative DP solution
  ==============================

  dp[l][b] = maximal joltage with prefix bank[0...l] within budget b

  dp[l][b] = max(
    dp[l-1][b-1]*10 + bank[l],
    dp[l-1][b]
  )

  dp[0][b] = bank[0]
  dp[l][0] = 0

  This basically follows the same principle as the greedy solution. This works because the greedy algorithm is correct and optimal.
*/
long long seek_best_dp(const vector<int>& bank, int budget) {
  int l = bank.size(), b = budget;

  vector<vector<long long>> dp(l, vector<long long>(b+1, 0));

  for(int i=1; i<=b; i++)
    dp[0][i] = bank[0];

  for(int i=1; i<l; i++)
    for(int j=1; j<=b; j++)
      dp[i][j] = max(dp[i-1][j-1] * 10 + bank[i], dp[i-1][j]);

  return dp[l-1][b];
}