class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n <= 1: return [nums]
        
        perms = []
        
        def directed_perm(index, so_far):
            if index == n:
                perms.append(so_far)
                return
            
            for i in range(index, n):
                # swap i and index
                nums[i], nums[index] = nums[index], nums[i]
                directed_perm(index+1, so_far + [nums[index]])
                # revert the swap before we try next swap
                nums[i], nums[index] = nums[index], nums[i]
            return
        
        directed_perm(0, [])
        return perms
