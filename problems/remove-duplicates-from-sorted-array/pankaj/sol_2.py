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
        cur = 1 # cur = 0 is trivially uniq
        last_uniq = 0
        
        while cur < n:
            while cur < n and nums[cur] == nums[last_uniq]:
                cur += 1
            # we have a new uniq
            if cur < n:
                last_uniq += 1
                nums[last_uniq] = nums[cur]
        return last_uniq + 1
        
        

