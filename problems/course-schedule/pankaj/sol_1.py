from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Is there a topological sort spanning all courses?

        Use a queue.

        Initially put all nodes with no incoming edges. This is done by keeping weight calculation.


        Remove one node from queue (break if q is empty)
        Mark it visited. Remove weight contribution of all edges outgoing from current edge.
        From all non-visited nodes, find nodes with incoming weight = 0 and put in q.

        Continue till q is empty.

        Are all nodes visited?
        """
        
        in_weights = defaultdict(int)

        for edge in prerequisites:
            later, earlier = edge[0], edge[1]
            in_weights[later] += 1

        # print("in_weights are ", in_weights)
        q = []
        visited = {}
        for course in range(numCourses):
            visited[course] = False
            if in_weights[course] == 0:
                q.append(course)

        print("Initially q is ", q)
        order = []
        while len(q) > 0:
            cur = q.pop(0)
            if visited[cur]:
                continue
            order.append(cur)
            visited[cur] = True

            # update in_weights for all nodes to which there is an edge from cur
            for edge in prerequisites:
                later, earlier = edge[0], edge[1]
                if earlier == cur:
                    in_weights[later] -= 1
            
            # print("Updated weights: ", in_weights)
            # find next possible set of nodes to be put in the q.
            for course in range(numCourses):
                if in_weights[course] == 0 and not visited[course]:
                    q.append(course)

        # Have we visited all the nodes?
        # print('finally visited is ', visited)
        c1, c2 = 0, 0
        for k in visited:
            if visited[k]:
                c1 += 1
            else:
                c2 += 1
        print(c1, c2)
        print(order)
        return all(visited.values())


        
