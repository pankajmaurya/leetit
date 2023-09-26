class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n <= 1: return [nums]
        
        perms = []
        
        def directed_perm(index, sofar):
            if index == n:
                perms.append(sofar)
                return
            choices_made = set()
            for i in range(index, n):
                if nums[i] not in choices_made:
                    choices_made.add(nums[i])
                    nums[i], nums[index] = nums[index], nums[i]
                    directed_perm(index+1, sofar+[nums[index]])
                    nums[i], nums[index] = nums[index], nums[i]
        directed_perm(0, [])
        
        return perms
