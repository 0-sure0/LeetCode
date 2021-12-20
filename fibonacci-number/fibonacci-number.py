class Solution:
    def fib(self, n: int) -> int:
        fib_dp = [0, 1]
        
        if n <= 1:
            return fib_dp[n]
        
        for i in range(2, n + 1):
            fib_dp.append(fib_dp[i-1] + fib_dp[i-2])
        
        return fib_dp[n]
            