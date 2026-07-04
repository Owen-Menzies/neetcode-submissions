from _heapq import heappop
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = -sum(height)
        running = 0
        while left <= right:
            if height[left] > running and height[right] > running:
                total += right - left + 1
                running += 1
            elif height[left] <= running:
                left += 1
            else:
                right -= 1
        return total


        # biggest = max(height)
        # total = biggest* len(height) - sum(height)
        # left = 0
        # cur_big = 0
        # while height[left] != biggest: 
        #     cur_big = max(cur_big,height[left])
        #     left += 1
        #     total -= (biggest - cur_big)
        # right = len(height) - 1
        # cur_big = 0
        # while height[right] != biggest: 
        #     cur_big = max(cur_big,height[right])
        #     right -= 1
        #     total -= (biggest  - cur_big)
        # return total
        