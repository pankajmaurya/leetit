# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/283/
# Had done this
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n = len(nums)
        
        def twoSum(targetIndex):
            target = -1 * nums[targetIndex]
            l, r = targetIndex + 1, n-1
            ans = []
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append((l,r))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
            return ans
            
        threes = set()
        for i in range(n):
            pairs = twoSum(i)
            if pairs:
                for pair in pairs:
                    l,r = pair 
                    threes.add(tuple([nums[i], nums[l], nums[r]]))
        return threes
                
            
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))      

