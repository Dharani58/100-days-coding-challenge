class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_streak = 0
        current_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 0
        return max(max_streak, current_streak)
solver = Solution()
input_array = [1, 1, 0, 1, 1, 1]
result = solver.findMaxConsecutiveOnes(input_array)
print(f"Input: {input_array}")
print(f"Result: {result}")