class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []
        for char in tokens:
            if char.isnumeric():
                sta.append(int(char))

            elif char == "+":
                sta[-2] += sta[-1] 
                sta.pop()
            elif char == "-":
                sta[-2] -= sta[-1]
                sta.pop()
            elif char == "*":
                sta[-2] *= sta[-1]
                sta.pop()
            elif char == "/":
                sta[-2] /= sta[-1]
                sta.pop()
                sta[-1] = int(sta[-1])
            else:
                sta.append(int(char))
        return sta[0]