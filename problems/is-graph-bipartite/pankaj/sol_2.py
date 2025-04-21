class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)

        visited = [False] * n
        color_opt = [0] * n

        def check_neighbours(node):
            red_mask = 1
            green_mask = 2
            red = 0
            green = 0
            # print(f'check_neighbours for {node}')
            for nei in graph[node]:
                if color_opt[nei] != 0:
                    if not red:
                        red = red_mask & color_opt[nei]
                    if not green:
                        green = green_mask & color_opt[nei]
            return red | green


        def visit(node):
            # print(f'Attempt to visit {node}')
            if visited[node]:
                # print(f'already visited {node}')
                return True
            visited[node] = True
            
            # pick_color, mask = check_neighbours(node)
            mask = check_neighbours(node)
            # print(f'color chosen is {pick_color}')
            # if pick_color == 'both':
            if mask == 3:
                # print(f'mask was {mask}')
                return False
            
            if mask == 0:
                # pick_color = 'red'
                mask = 1
            
            for nei in graph[node]:
                # if color[nei] is None:
                if color_opt[nei] == 0:
                    # print(f'coloring {nei} : the neighbour of {node} to {pick_color}')
                    # color[nei] = pick_color
                    # color_opt[nei] = color_map[pick_color]
                    color_opt[nei] = mask

            # visited[node] = True
            # color[node] = 'green' if pick_color == 'red' else 'red'
            color_opt[node] = 3 - mask #color_map[color[node]]
            # print(f'Marking {node} as visited now., colors are {color_opt}')
            return True

        def bfs_visit(node):
            if visited[node]:
                return True

            q = []
            q.append(node)

            while len(q) > 0:
                cur = q.pop(0)
                if not visit(cur):
                    return False
                for nei in graph[cur]:
                    if not visited[nei]:
                        q.append(nei)
            return True

        # Do a bfs visit on all nodes
        for i in range(n):
            if not visited[i]:
                if not bfs_visit(i):
                    return False

        return True
        