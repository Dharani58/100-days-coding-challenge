class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k

solver = Solution()
nums_input = [1, 12, -5, -6, 50, 3]
k_input = 4
result = solver.findMaxAverage(nums_input, k_input)
print(f"Input Nums: {nums_input}, k: {k_input}")
print(f"Maximum Average: {result}")