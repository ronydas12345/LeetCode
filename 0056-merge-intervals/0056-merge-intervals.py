class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = itemgetter(0))
        res = [intervals[0]]

        for i in intervals:
            if res[-1][1] >= i[0]:
                res[-1] = [res[-1][0], max(i[1], res[-1][1])]
            else:
                res.append(i)
        
        return res
