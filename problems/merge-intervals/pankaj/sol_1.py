class Interval(object):
    def __init__(self, s, e):
        self.s = s
        self.e = e
        
    def __lt__(self, other):
        if self.s < other.s:
            return True
        elif self.s == other.s:
            return self.e <= other.e
        else:
            return False
    
    def __repr__(self):
        return "[{}, {}]".format(self.s, self.e)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
#         arr = []
#         for i in intervals:
#             arr.append(Interval(i[0], i[1]))
#         arr.sort()
        
        arr = sorted(map(lambda pair: Interval(pair[0], pair[1]), intervals))
        prev = arr[0]
        final = []
        for cur in arr[1:]:
            if cur.s <= prev.e:
                prev.e = max(cur.e, prev.e)
            else:
                final.append(prev)
                prev = cur
        if prev not in final:
            final.append(prev)
        # # if cur not in final:
        # #     final.append(cur)
        # print(arr)
        # print(final)
        return [[f.s, f.e] for f in final]
