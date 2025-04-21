class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(f'n is {n}')
        # case of only 1 number
        if n == 1:
            return

        a = nums[0]
        # special case of all numbers same
        v = [nums[i] == a for i in range(1, n)]
        print(f"v is {v}")
        if all([nums[i] == a for i in range(1, n)]):
            return

        # We have some non zero work from here.
        # lets partition nums into 2 parts - one which does not change and one which does
        # the first place of change will be when the first number is found which is lesser than to its right
        # e.g. 2 1 1 4 3 3 => change will be in thousands place
        # 2 1 3 x x x
        position = None
        start = int(n - 2)
        for i in range(start, -1, -1):
            print(f'checking for position at {i}')
            if nums[i] < nums[i+1]:
                position = i
                break
        
        print(f"position is {position}")
        # what if position remains none? 
        if position is None:
            # entire array should be swapped.
            for i in range(0, int(n/2)):
                nums[i], nums[n - 1 - i] = nums[n-1-i], nums[i]
            return

        # Once we have decided the position the number which will come in its place will
        # be the smallest number larger than current one at position
        cur = nums[position]
        # scan from lowest to position + 1 to find the smallest number which is larger than cur
        swap_pos = None
        for i in range(n-1, position, -1):
            if nums[i] > cur:
                swap_pos = i
                break

        # do the swap
        nums[position], nums[swap_pos] = nums[swap_pos], nums[position]

        # now the part of the array after position must be reversed.
        swap_count = 0
        mid = int((n -1 + (position + 1))/2)
        for i in range(position + 1, mid + 1):
            nums[i], nums[n-1 - swap_count] = nums[n-1 - swap_count], nums[i]
            swap_count += 1
        return