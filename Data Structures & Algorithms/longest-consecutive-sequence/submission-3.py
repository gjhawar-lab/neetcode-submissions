class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique_nums = set(nums)
        max_seq = 0

        for num in unique_nums:
            if num - 1 not in unique_nums:
                length = 1
                while num + length in unique_nums:
                    length += 1
                max_seq = max(max_seq, length)
        
        return max_seq