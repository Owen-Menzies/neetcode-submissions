class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for _ in range(len(temperatures))]
        current_index = 0
        for index, temp in enumerate(temperatures):
            if stack and temp > stack[-1][0]:
                current_index = 0
                while len(stack) > 0 and stack[-1][0] < temp:
                    current_index += 1
                    res[stack[-1][1]] = index - stack[-1][1]
                    stack.pop()

            stack.append((temp,index))
        return res