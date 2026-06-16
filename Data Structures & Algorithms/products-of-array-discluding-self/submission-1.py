class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = {}

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i !=  j:
                    total *= nums[j]
            d[i] =  total
        output = [d[i] for i in range(len(nums))]
        return output

        