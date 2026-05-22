class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in seen_values:
                return [seen_values[difference], i]
            seen_values[n] = i
        raise ValueError("no solution")  # ← what the test expects