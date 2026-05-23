class Solution:
    #Bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Create buckets where index = frequency
        # Max possible frequency is len(nums), so we need len(nums)+1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Put each number into its frequency bucket
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Step 4: Collect k elements starting from highest frequency
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # go backwards (high to low freq)
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
