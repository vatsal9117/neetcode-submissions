class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_int = intervals[0]
        num_removals = 0
        for inter in intervals[1:]:
            start, end = inter
            if prev_int[0] <= start < prev_int[1]:
                # use smaller interval or interval that comes first if same size
                if prev_int[1] > end:
                    prev_int = [start, end]
                num_removals += 1
            else:
                prev_int = [start, end]
        return num_removals 

        # (1,2), (1,4), (2,4)
