class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        snums = set(numbers)
        for i in range(len(numbers)):
            if target- numbers[i] in snums:
                return [i+1, 1 + numbers.index(target-numbers[i])]