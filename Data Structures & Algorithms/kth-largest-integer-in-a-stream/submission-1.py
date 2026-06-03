class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:]
        self.k = k

        # Heapify
        heapq.heapify(self.heap)
        # Pop till heap is right size
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
        # if heap is full and new val is greater than top, pop the smallest element and add the new val
            heapq.heappop(self.heap)

        return self.heap[0]