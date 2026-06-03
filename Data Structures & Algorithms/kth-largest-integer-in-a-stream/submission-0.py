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
        # if heap is not full push element to it
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val :
        # if heap is full and new val is greater than top, pop the smallest element and add the new val
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
