class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        num_map = {} # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement],i]
            num_map[num] = i
        return []





        