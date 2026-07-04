class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right  = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left+1)//2 
            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle 
        return left if nums[left] == target else -1 