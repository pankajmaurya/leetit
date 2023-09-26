class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1.sort()
        nums2.sort()
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        out = set()
        while p1 < n1 and p2 < n2:
            if nums1[p1] == nums2[p2]:
                out.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return out
