from collections import defaultdict
import itertools
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0: return ""
        if len(words) == 1: return words[0]
        x = [list(w) for w in words]
        alphabet = set(itertools.chain(*x))
                
        graph = defaultdict(list)
        for (first, second) in zip(words, words[1:]):
            if first.startswith(second) and len(first) > len(second):
                return ""
            else:
                lf,ls = len(first), len(second)
                i, j = 0, 0
                while i < lf and j < ls:
                    if first[i] != second[j]:
                        # capture edge from first[i] -> second[j]
                        graph[first[i]].append(second[j])
                        break
                    else:
                        i += 1
                        j += 1
        # create a q with all letters with no incoming edges
        counts = defaultdict(int)
        for destinations in graph.values():
            for d in destinations:
                counts[d] += 1
        q = []
        for letter in alphabet:
            if counts[letter] == 0:
                q.append(letter)
        
        # q.sort()
        # Do topological sort generating the answer.
        # If after topological sort, we have less letters than alphabet, indicative of cycle.
        ans = []
        while q:
            letter = q.pop(0)
            ans.append(letter)
            for dest in graph[letter]:
                counts[dest] -= 1
                if counts[dest] == 0:
                    q.append(dest)
            
        
        return "" if len(ans) < len(alphabet) else ''.join(ans)
