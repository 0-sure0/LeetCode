class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 1 or len(prerequisites) == 0:
            return True
        
        course = collections.defaultdict(list)
        visit = [0] * numCourses
        
        for p in prerequisites:
            course[p[0]].append(p[1])

        def dfs(c):
            if visit[c] == -1:
                return False
            if visit[c] == 1:
                return True
            
            visit[c] = -1
            for pre in course[c]:
                if not dfs(pre):
                    return False
            visit[c] = 1
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True