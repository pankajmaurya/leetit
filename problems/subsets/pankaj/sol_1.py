class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        out = []
        def directed_subsets(cur_pos, subset_so_far):
            # print('calling for cur_pos', cur_pos, ' with subset_so_far', subset_so_far)
            if cur_pos == n:
                out.append(subset_so_far)
                return
            
            # case 1: include nums[cur_pos]
            directed_subsets(cur_pos+1, subset_so_far + [nums[cur_pos]])
            # case 2: do not include nums[cur_pos]
            directed_subsets(cur_pos+1, subset_so_far)
            
        directed_subsets(0, [])
        
        return out
