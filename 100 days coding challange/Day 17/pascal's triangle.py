class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        triangle = [[1]]
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            current_row = [1]
            for j in range(len(prev_row) - 1):
                current_row.append(prev_row[j] + prev_row[j + 1])
            current_row.append(1)
            triangle.append(current_row)
        return triangle

solver = Solution()
result = solver.generate(5)
for row in result:
    print(row)