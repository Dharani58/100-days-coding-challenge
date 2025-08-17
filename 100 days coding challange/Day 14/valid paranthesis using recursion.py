class Solution:
    def isValid(self, s):
        if not s:
            return True
        if "()" in s:
            return self.isValid(s.replace("()", "", 1))
        if "[]" in s:
            return self.isValid(s.replace("[]", "", 1))
        if "{}" in s:
            return self.isValid(s.replace("{}", "", 1))
        return False
solver = Solution()
user_string = input("Enter a string of parentheses (e.g., {[()]}): ")
result = solver.isValid(user_string)
if result:
    print(f"The string '{user_string}' is valid.")
else:
    print(f"The string '{user_string}' is not valid.")