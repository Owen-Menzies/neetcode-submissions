class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 
        heaps = []
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        for keys,values in dic.items():
            heaps.append((values,keys))
        heapq._heapify_max(heaps)
        # heapq.heapify(lambda x:x[1])
        results = []
        for i in range(k):
            results.append(heapq.heappop_max(heaps)[1])
            
        return results