class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = text1
        s2 = text2
        cache = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    cache[i+1][j+1] = cache[i][j] + 1 
                else:
                    cache[i+1][j+1] = max(cache[i+1][j], cache[i][j+1])
        return cache[-1][-1]
        i, j = len(s1) - 1,len(s2) - 1
        sub = ""
        while i >= 0 and j >= 0:            
            if cache[i+1][j] == cache[i+1][j+1]:
                j -= 1
            elif cache[i][j+1] == cache[i+1][j+1]:
                i -= 1
            else:
                i -= 1
                j -= 1
                sub = s1[i+1] + sub 
        return len(sub)