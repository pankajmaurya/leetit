class Solution(object):
    def shortestDistance(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        For each point in grid which is a 'building' start a bfs. update reachability stats and cost of reaching for each point in the grid which is an empty space.
        
        Once we have done this, which empty space has the reachability for all buildings and the min cost?
        """
        if not g: return -1
        m = len(g)
        if m == 0: return -1
        n = len(g[0])
        if n == 0: return -1
        
        buildings = []
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    buildings.append((i, j))
        
        CostMatrix = [[0 for x in range(n)] for y in range(m)] 
        ReachCountMatrix = [[0 for x in range(n)] for y in range(m)]
        
        # print(CostMatrix)
        
        # bfs starting from building b.
        def bfs(b):
            # put node and cost of reachability
            q = [(b, 0)]
            visited = {}
            visited[b] = True
            CostMatrix[b[0]][b[1]] = 0
            while q:
                cur, cost = q.pop(0)
                x, y = cur
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        newx = x+dx
                        newy = y+dy
                        
                        if g[newx][newy] != 0:
                            continue
                            
                        p = (newx,newy)
                        if p not in visited:
                            visited[p] = True
                            CostMatrix[newx][newy] += (cost + 1)
                            ReachCountMatrix[newx][newy] += 1
                            q.append((p, cost+1))
                            
        for building in buildings:
            # print('processing building ', building)
            bfs(building)
            # print('ReachCountMatrix', ReachCountMatrix)
            # print('CostMatrix', CostMatrix)
            
        min_cost = float('inf')
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0 and ReachCountMatrix[i][j] == len(buildings) and CostMatrix[i][j] < min_cost:
                    min_cost = CostMatrix[i][j]
                    
        if min_cost == float('inf'):
            return -1
        else:
            return min_cost
