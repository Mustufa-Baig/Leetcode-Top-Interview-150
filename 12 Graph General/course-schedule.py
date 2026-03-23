from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        def dfs(course: int) -> bool:
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
