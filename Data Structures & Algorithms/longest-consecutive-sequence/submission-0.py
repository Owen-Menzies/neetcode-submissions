class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for i in set_nums:
            if i - 1 not in set_nums:
                new_long = 1
                while i + 1 in set_nums:
                    new_long+=1
                    i += 1
                longest = max(longest,new_long)
        return longest