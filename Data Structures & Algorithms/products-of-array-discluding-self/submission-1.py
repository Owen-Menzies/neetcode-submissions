class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] * prefix[i-1])
            print(suffix[i-1])
            suffix.append(nums[len(nums) - i-1] * suffix[i-1])
        suffix.reverse()
        res = [suffix[1]]
        res.extend([prefix[i-1] * suffix[i + 1] for i in range(1,len(nums)-1)])
        res.append(prefix[-2])
        print(prefix)
        # suffix.reverse
        print(suffix)
        return res
        


