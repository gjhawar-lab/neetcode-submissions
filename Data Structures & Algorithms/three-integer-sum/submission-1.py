class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort so two pointers work and duplicates are adjacent
        # [-1,0,1,2,-1,-4] → [-4,-1,-1,0,1,2]
        nums.sort()
        output = []

        # Step 2: Fix the first number at index i
        for i in range(len(nums)):
            # After sorting, if nums[i] > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for i to avoid duplicate triplets
            # e.g. [-1, -1, 0, 1] — only process the first -1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Two pointers — l starts after i, r at end
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    # Sum too small — need a larger number, move l right
                    l += 1
                elif total > 0:
                    # Sum too large — need a smaller number, move r left
                    r -= 1
                else:
                    # Found a valid triplet
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return output