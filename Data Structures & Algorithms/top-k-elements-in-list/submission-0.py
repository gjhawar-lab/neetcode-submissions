class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            freq_dict = {}

            for num in nums:
                freq_dict[num] = freq_dict.get(num, 0) + 1
                
            sorted_keys = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)
            return sorted_keys[:k]
