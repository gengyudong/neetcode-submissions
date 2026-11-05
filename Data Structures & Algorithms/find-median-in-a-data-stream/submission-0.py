import heapq

class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.big_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half, -num)
        heapq.heappush(self.big_half, -heapq.heappop(self.small_half))
        if len(self.big_half) > len(self.small_half):
            heapq.heappush(self.small_half, -heapq.heappop(self.big_half))

    def findMedian(self) -> float:
        if len(self.small_half) != len(self.big_half):
            median = -self.small_half[0]
            return median
        else:
            num_one = -self.small_half[0]
            num_two = self.big_half[0]
            median = (num_one + num_two) / 2
            return median
        
        