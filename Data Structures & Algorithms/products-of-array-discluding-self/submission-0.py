class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        postfix_product = [1] * len(nums)
        output = [1] * len(nums)

        """
        example : nums =  [1, 2, 4, 6]
        prefix_product =  [1, 2, 8, 48]
        postfix_product = [48, 48, 24, 6]
        output = [48, 24, 12 , 8]
        """
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        
        
        for i in range(len(nums) - 2 , -1, -1):
            postfix_product[i] = postfix_product[i+1] * nums[i+1]


        for i in range(len(nums)):
            output[i] = prefix_product[i] * postfix_product[i]

        return output     
            