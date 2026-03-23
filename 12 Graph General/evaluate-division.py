class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        result = []
        
        for query in queries:
            result.append(self.getPathWeight(query[0], query[1], set(), graph))
        
        return result
    
    def getPathWeight(self, start, end, visited, graph):
        if start not in graph:
            return -1.0
        
        if start == end:
            return 1.0
        
        visited.add(start)
        for neighbour, weight in graph[start].items():
            if neighbour not in visited:
                productWeight = self.getPathWeight(neighbour, end, visited, graph)
                if productWeight != -1.0:
                    return weight * productWeight
        
        return -1.0
    
    def buildGraph(self, equations, values):
        graph = {}
        
        for i in range(len(equations)):
            u, v = equations[i]
            graph.setdefault(u, {})
            graph[u][v] = values[i]
            graph.setdefault(v, {})
            graph[v][u] = 1 / values[i]
        
        return graph
