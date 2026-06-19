class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            next_val = prev + curr
            prev = curr
            curr = next_val
        return curr
