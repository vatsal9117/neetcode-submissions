class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i +1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j+ 1]
        # return []
        numSet = defaultdict(int)
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if numSet[complement] :
                return [numSet[complement], i + 1]
            numSet[numbers[i]] = i + 1
        return []
        