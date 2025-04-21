from collections import defaultdict
class Solution(object):

    def minWindowHelper(self, s, t_map, start_s):
        """
        t_map is a map of unique characters in t to their counts
        start_s is 0 index based

        Returns (pos of minWindow end, minWindow)
        pos of min Window end is 0 index based.
        """
        s_map = defaultdict(int)
        for i, c in enumerate(s[start_s:]):
            if c not in t_map:
                continue
            s_map[c] = 1 if c not in s_map else s_map[c] + 1
            # we know we updated s_map
            if all([s_map[i] >= t_map[i] for i in t_map]):
                # stop here
                return i, s[start_s: i+1]
        return -1, ""


    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        We solve 2 smaller problems:

        problem 1: find the minWindow(s, t, start_pos_in_s)
        Let this return the mininum window substring of s[start_pos_in_s:]
        containing all characters of t in any order + necessarily starting at start_pos_in_s.


        problem 2: given output of minWindow(s, t, start_pos_in_s)
        find minWindow(s, t, start_pos_in_s + 1)

        To solve 2, we divide it into 2 cases:
        Case: s[start_pos_in_s] is not in t 
        minWindow(s, t, start_pos_in_s + 1)=minWindow(s, t, start_pos_in_s)[1:]
        Case: s[start_pos_in_s] is in t 
        say, c = s[start_pos_in_s]
        Then, we have to look for c beyond minWindow(s, t, start_pos_in_s)

        Say we find it in some position x (x being 1 indexed)
        Then we return the minimum window as 
        minWindow(s, t, start_pos_in_s)[1:] + s[start_pos_in_s+len(minWindow(s, t, start_pos_in_s)):x]

        that is, skip the first character of last window and go past its end till character x

        Globally we can maintain a variable answer to record the minimum window substring.
        """
        t_map = {}
        for x in t:
            t_map[x] = 1 if x not in t_map else t_map[x] + 1

        if len(s) == 0:
            return ""

        end, answer = self.minWindowHelper(s, t_map, 0)
        print(f"initial run at 0 gave {end} {answer}")
        current_window = answer

        if len(s) == 1:
            return answer

        m = len(s)
        n = len(t)

        for i in range(1, m - n):
            # All valid possible starts, we have already handled start = 0
            if s[i-1] not in t_map:
                # end = end
                current_window = answer[1:]
                answer = current_window if len(current_window) < len(answer) else answer
            else:
                for x, c in enumerate(s[end+1:]):
                    if c == s[i-1]:
                        current_window = s[i:len(current_window)+x+1]
                        answer = current_window if len(current_window) < len(answer) else answer
                        break
        return answer

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
