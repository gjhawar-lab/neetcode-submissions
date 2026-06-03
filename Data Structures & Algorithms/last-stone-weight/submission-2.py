class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Build max-heap by negating
        heap = [-s for s in stones]
        heapq.heapify(heap)

        # Pop the max
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(x - y))

        return -heap[0] if heap else 0
        