import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        output = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                output.append(num)
                if len(output) == k:
                    return output
        
        return output
        