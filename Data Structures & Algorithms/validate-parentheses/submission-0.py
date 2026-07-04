class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        open_ = "([{"
        dic = {"}":"{" ,"]":"[" , ")":"("}
        for i in s:
            if i in open_:
                res.append(i)
            else: 
                if len(res) == 0 or dic[i] != res[-1] :
                    return False
                res.pop()
        return len(res) == 0
