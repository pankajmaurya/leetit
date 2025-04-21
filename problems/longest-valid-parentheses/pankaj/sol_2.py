class Solution:

    # Case of (()()) => 3 pops, outer pop solved by : i - pos + 1
    # Case of ()() => 2 pops, first pop solved by i - pos + 1, 2nd pop

    # Negative case: ()(() => 2 pops, 
    # Negative case (()() => 2 pops
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        cur_len = 0
        min_pos = None
        start = None
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((i, c))
            else:
                # can we pop? only when we have a left parentheses
                top_pos, top_char = None, None
                if len(stack) > 0:
                    top_pos, top_char = stack[-1]
                if top_char == '(':
                    pos, _ = stack.pop()

                    if start is None:
                        start = pos
                    if pos < start:
                        start = pos

                    if len(stack) == 0:
                        # We have emptied the stack => len = i - pos + 1
                        cur_len = i - start + 1
                    else:
                        # the length of the matching string extends from last pos on stack to i
                        top, _ = stack[-1]
                        cur_len = i - top
                    ans = max(ans, cur_len)
                else:
                    stack.append((i, c))
                    start = None
        return ans
        
