class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # snums = set(numbers)
        # for i in range(len(numbers)):
        #     if target- numbers[i] in snums:
        #         return [i+1, 1 + numbers.index(target-numbers[i])]

        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i+1,j+1]