class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Example 1: nums = [3, 4, 5, 6, 1, 2], target = 1  (target in unsorted half)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                # LEFT HALF IS SORTED — range check against [nums[l], nums[mid])
                # Example: sorted=[3,4,5], target=1 → 1 in [3,5)? No → search right
                # Example: sorted=[4,5,6,7], target=5 → 5 in [4,7)? Yes → search left
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # RIGHT HALF IS SORTED — range check against (nums[mid], nums[r]]
                # Example: sorted=[1,2], target=2 → 2 in (1,2]? Yes → search right
                # Example: sorted=[2,3,4], target=6 → 6 in (1,4]? No → search left
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
            