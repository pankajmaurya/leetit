"""
When a room is taken, the room can not be used for anther meeting until the current meeting is over. As soon as the current meeting is finished, the room can be used for another meeting. We can sort the meetings by start timestamps and sequentially assign each meeting to a room. Each time when we assign a room for a meeting, we check if any meeting is finished so that the room can be reused. In order to efficiently track the earliest ending meeting, we can use a min heap. Whenever an old meeting ends before a new meeting starts, we reuse the room (i.e., do not add more room). Otherwise, we need an extra room (i.e., add a room).
"""
import heapq

class Interval(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r
        
    def __lt__(self, o):
        return self.l < o.l or (self.l == o.l and self.r <= o.r)
    
    def __str__(self):
        return "[{}, {}]".format(self.l, self.r)

    def __repr__(self):
        return "[{}, {}]".format(self.l, self.r)

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        ilist = []
        if len(intervals) <= 1:
            return len(intervals)
        
        for i in intervals:
            ilist.append(Interval(i[0], i[1]))
            
        ilist.sort()
        print(ilist)
        
        rooms = 1
        end_times_min_heap = []
        heapq.heappush(end_times_min_heap, ilist[0].r)
        
        for i in ilist[1:]:
            cur_start = i.l
            cur_end = i.r
            # earliest end time will be in end_times_min_heap[0]
            if cur_start >= end_times_min_heap[0]:
                # we can reuse the same room
                heapq.heappushpop(end_times_min_heap, cur_end)
            else:
                # need to add a room to accomodate this meeting
                rooms += 1
                heapq.heappush(end_times_min_heap, cur_end)
                
        return rooms
