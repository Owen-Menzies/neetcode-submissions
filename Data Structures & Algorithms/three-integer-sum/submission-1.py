class Solution:

    def twoSum(self, numbers, target,exclude):
        i = 0
        j = len(numbers) - 1
        while i < len(numbers) and j >= 0 and i != j:
            if i in exclude:
                i +=1 
                
            elif j in exclude:
                j -= 1
            
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            
            else:
                return (i,j)
            
        return None

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        res = []
        for i in range(len(snums)):
            exclusions = [i]
            cords = self.twoSum(snums,0-snums[i],exclusions) 

            while cords is not None:
                candidate = sorted([snums[i],snums[cords[0]],snums[cords[1]]])
                # print(res)
                if candidate not in res:
                    res.append(candidate)
                exclusions.extend([cords[0],cords[1]])
                cords = self.twoSum(snums,0-snums[i],exclusions) 
        return res
