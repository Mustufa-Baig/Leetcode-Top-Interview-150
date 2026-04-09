class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def get_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:
                return float('inf')
            return (y2 - y1) / (x2 - x1)
        
        res = 0
        for i in range(len(points)):
            slope_map = {}
            same_point = 1
            for j in range(i + 1, len(points)):
                if points[j] == points[i]:
                    same_point += 1
                    continue
                slope = get_slope(points[i], points[j])
                slope_map[slope] = slope_map.get(slope, 0) + 1
            res = max(res, max(slope_map.values(), default=0) + same_point)
        return res