class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int

        We implement a sliding window approach
        """
        n = len(s)

        if n <= 1:
            return n
        
        d = defaultdict(int)
        l, r = 0, 1 # left and right, left in inclusive, right is exclusive
        d[s[0]] = 1

        ans = 1
        
        while r < n and l < r:
            # try to expand first
            d[s[r]] += 1
            r += 1
            while not all([d[i] <= 1 for i in d]) and l < r:
                print(f"Contracting string {l}, {r}:  {s[l:r]}")
                l += 1
                d[s[l-1]] -= 1
            ans = max(ans, r - l)
        return ans
        
