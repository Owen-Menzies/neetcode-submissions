class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for _ in range(len(temperatures))]
 
        for index, temp in enumerate(temperatures):
            
            while stack and stack[-1][0] < temp:
       
                res[stack[-1][1]] = index - stack[-1][1]
                stack.pop()

            stack.append((temp,index))
        return res