class Solution:
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
solver = Solution()
user_input_string = input("Enter a string of parentheses (e.g., {[()]}): ")
is_valid_result = solver.isValid(user_input_string)
if is_valid_result:
    print(f"The string '{user_input_string}' is valid.")
else:
    print(f"The string '{user_input_string}' is not valid.")