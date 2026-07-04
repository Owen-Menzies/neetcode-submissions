class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        p = [x.lower() for x in s if x.isalnum()]
        # print(p)
        j = p[:]
        p.reverse()
        return j == p