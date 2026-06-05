class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seet = set()
        for i in nums:
            if i in seet:
                seet.remove(i)
            else:
                seet.add(i)
        return list(seet)[0]

        