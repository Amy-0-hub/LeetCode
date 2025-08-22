class Solution:
    def fib(self, n: int) -> int:
        # given n, return the n'th number in fibonaccio series
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


print(Solution().fib(4))
