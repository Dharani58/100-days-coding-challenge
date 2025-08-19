class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        two_steps_back = 1
        one_step_back = 2
        for _ in range(3, n + 1):
            current_ways = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current_ways
        return one_step_back
solver = Solution()
num_stairs = 5
result = solver.climbStairs(num_stairs)
print(f"Number of ways to climb {num_stairs} stairs: {result}")