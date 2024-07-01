

class Solution:

    def creatingUndirectedGraph(self, n: int, edges: list[list[int]]):
        #  n = 4 
        # edges = [[1,0],[1,2],[1,3]]
        
        G = {i: [] for i in range(n)}

        for a, b in edges:
            G[a].append(b)
            G[b].append(a)
            
        return G

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        G = self.creatingUndirectedGraph(n, edges)

        def dfs(temp, h=0, vis=set(), zamax=0):
            child = list(set(G[temp]) - vis)
            vis.add(temp)
            if not child:
                return h
            for ch in child:
                zamax = max(zamax, dfs(ch, h + 1, vis, zamax))

            return zamax
        
        zamin = []
        for i in range(n):
            zamin.append(dfs(i))
        return min(zamin)