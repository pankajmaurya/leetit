"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        
        # do a bfs traversal starting from node
        clone_dict = {}
        def cloneNode(cur): 
            clone_dict[cur] = Node(cur.val)
            
        def populateNeighborsForClone(cur):
            clone_dict[cur].neighbors.extend([clone_dict[n] for n in cur.neighbors])
                
        def bfsTraversal(startnode, visit_fn):
            q = [startnode]
            state = {}
            state[startnode] = "discovered"
            while q:
                cur = q.pop(0)
                visit_fn(cur)
                for neighbor in cur.neighbors:
                    if neighbor not in state:
                        state[neighbor] = "discovered"
                        q.append(neighbor)
                state[cur] = "processed"
        
        bfsTraversal(node, cloneNode)
        setattr(Node, '__repr__', lambda x: str(x.val))
        print(clone_dict.keys())
        bfsTraversal(node, populateNeighborsForClone)
        return clone_dict[node]
