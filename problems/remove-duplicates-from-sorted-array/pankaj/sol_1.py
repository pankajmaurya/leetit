# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3011/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        n = len(nums)
        # Everything from 0 to uniq_end (excluded) is uniq
        uniq_end = 1
        
        cur = uniq_end
        # cur = n => we are beyond end of nums
        while cur < n:
            while cur < n and nums[cur] == nums[uniq_end-1]:
                cur += 1
            # now cur is uniq again.
            if cur < n:
                nums[uniq_end] = nums[cur]
                uniq_end += 1
        return uniq_end
        
        

