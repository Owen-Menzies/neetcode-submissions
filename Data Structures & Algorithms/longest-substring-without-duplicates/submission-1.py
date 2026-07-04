class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        left = 0
        right = 0
        max_length = 0
        while left < len(s) - max_length:
            if right < len(s) and s[right] not in unique_set:
                unique_set.add(s[right])
                right += 1
            else:
                max_length = max(max_length,right-left)
                left += 1
                right = left
                
                unique_set = set()
        return max_length