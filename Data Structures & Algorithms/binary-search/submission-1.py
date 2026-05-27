class Solution:
    # def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
    #     if l > r:
    #         return -1
    #     m = l + (r - l) // 2

    #     if nums[m] == target:
    #         return m
    #     if nums[m] < target:
    #         return self.binary_search(m + 1, r, nums, target)
    #     return self.binary_search(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        l,r =  0, len(nums)
        while l < r:
            m = l + ((r - l )//2)

            if nums[m] > target:
                r =  m 
            elif nums[m] <= target:
                l = m + 1
        return l - 1 if (l and nums[l - 1] ==  target) else -1