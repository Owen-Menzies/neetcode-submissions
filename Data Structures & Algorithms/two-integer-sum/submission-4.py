class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1 
        bums = nums[:]
        nums.sort()
        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            else: 
                i += 1
        p = bums.index(nums[i])
        bums.reverse()
        k = len(bums) - bums.index(nums[j]) -1
        return sorted([p,k])