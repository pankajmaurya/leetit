class Solution:
    def longestPalindrome(self, s: str) -> str:
        pals = set()

        n = len(s)

        if n <= 1:
            return s

        ans = s[0]
        # s = babad => ba, ab, ba, ad are len 2 substrings.
        # they are s[0:2], s[1:3], s[2:4] and s[3:5]
        # n = 5, start takes values {0, 1, 2, 3}. start is in range(0, 5 - 2 + 1)

        for l in range(2, n + 1):
            # l denotes the length of a substring
            for start in range(0, n - l + 1):
                end = start + l
                
                if s[start] == s[end - 1]:
                    # if l == 2, special case it.
                    if l == 2 or l == 3 or (start+1, end-1) in pals:
                        pals.add((start, end))
                        if l > len(ans):
                            ans = s[start:end]
        return ans

