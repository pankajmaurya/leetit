from collections import defaultdict
class Solution:

    def minWindowHelper(self, s: str, t_map: map, start_s: int) -> (int, str):
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
                return i, s[start_s: i+1], s_map
        return -1, ""

    def minWindow(self, s: str, t: str) -> str:    
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

        end, answer, s_map = self.minWindowHelper(s, t_map, 0)
        print(f"initial run at 0 gave {end} {answer}")
        current_window = answer

        if len(s) == 1:
            return answer

        m = len(s)
        n = len(t)

        for i in range(1, m - n + 1):
            # All valid possible starts, we have already handled start = 0
            if s[i-1] not in t_map:
                # end = end
                current_window = current_window[1:]
                answer = current_window if len(current_window) < len(answer) else answer
            else:
                s_map[s[i-1]] -= 1
                if s_map[s[i-1]] >= t_map[s[i-1]]:
                    current_window = current_window[1:]
                    answer = current_window if len(current_window) < len(answer) else answer
                else:
                    found=False
                    for x, c in enumerate(s[end+1:]):
                        if c in t_map:
                            s_map[c] += 1
                        if c == s[i-1]:
                            current_window = s[i:i+len(current_window)+x]
                            end = i + len(current_window) - 1
                            answer = current_window if len(current_window) < len(answer) else answer
                            found=True
                            break
                    # if we did not break out, it means we could not find a c = s[i-1]
                    if not found:
                        return answer
            print(f'For iteration at start position {i}, current_window is {current_window}, end is {end} and answer is now {answer}')
        return answer

s = Solution()
#print(s.minWindow("ADOBECODEBANC", "ABC"))
#print(s.minWindow("ab", "b"))
#print(s.minWindow("abc", "a"))
print(s.minWindow("cabefgecdaecf", "cae"))
        
