class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        sufix = {}

        p = 1
        for i in range(len(nums)):
            prefix[i] = p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            sufix[i] = p
            p *= nums[i]

        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i] * sufix[i])
        return answer
