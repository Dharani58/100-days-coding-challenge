import collections
class Solution:
    def minWindow(self, s,t):
        if not t or not s or len(s) < len(t):
            return ""
        t_counts = collections.Counter(t)
        left = 0
        have, need = 0, len(t_counts)
        result = [-1, -1]
        for right, char in enumerate(s):
            if char in t_counts:
                t_counts[char] -= 1
                if t_counts[char] == 0:
                    have += 1
            while have == need:
                current_len = right - left + 1
                if result[0] == -1 or current_len < result[0]:
                    result = [current_len, left]
                left_char = s[left]
                left += 1
                if left_char in t_counts:
                    if t_counts[left_char] == 0:
                        have -= 1
                    t_counts[left_char] += 1

        res_len, res_left = result
        return s[res_left: res_left + res_len] if res_len != -1 else ""

solver = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(f"The minimum window substring is: '{solver.minWindow(s, t)}'")