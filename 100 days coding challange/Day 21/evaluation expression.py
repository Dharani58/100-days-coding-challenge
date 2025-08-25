class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        last_operator = '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if not char.isdigit() and not char.isspace() or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    val = stack.pop()
                    stack.append(int(val / current_number))
                last_operator = char
                current_number = 0
        return sum(stack)