class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        color = {}
        vis = {}
        def dfs(n, cur_color):
            if n not in vis: 
                vis[n] = True
                if n in color and color[n] != cur_color:
                    return False
                elif n not in color:
                    color[n] = cur_color
                    
            
            next_color = 1 - cur_color
            
            for nbr in graph[n]:
                if nbr not in vis:
                    if not dfs(nbr, next_color):
                        return False
                else:
                    if color[nbr] != next_color:
                        return False
            return True
        
        for n in range(len(graph)):
            if n not in vis:
                if not dfs(n, 0):
                    return False
        return True
