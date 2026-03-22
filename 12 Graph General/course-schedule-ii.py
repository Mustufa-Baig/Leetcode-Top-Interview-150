from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == numCourses else []
