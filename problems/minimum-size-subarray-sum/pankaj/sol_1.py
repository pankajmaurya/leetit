class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0

        # we know that r can be atleast 1, our subarray is nums[l:r]
        l = 0
        r = 0

        # l = r implies that subarray is of size 0, hence we want l < r
        # once r reaches n, we cannot grow any further
        cur = 0
        ans = float('inf')
        while l <= r and r < n:
            # This explicit step ensures that in each iteration of outer loop we make progress.
            r += 1
            cur += nums[r - 1]
            while cur < target and r < n:
                r += 1
                cur += nums[r - 1]
            # now cur is atleast target
            while cur - nums[l] >= target and l <= r:
                l += 1
                cur -= nums[l - 1]

            if cur >= target:
                ans = min(ans, r - l)
        
        if ans == float('inf'):
            return 0
        return ans
            

