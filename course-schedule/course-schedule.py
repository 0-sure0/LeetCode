class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursedict = defaultdict(list)
        for cur, pre in prerequisites:
            coursedict[cur].append(pre)
        
        def isCyclic(current):
            if checked[current]:
                return False
            if path[current]:
                return True
            path[current] = True
            ret = False
            for child in coursedict[current]:
                ret = isCyclic(child)
                if ret:
                    break
            
            checked[current] = True
            path[current] = False
            return ret
        
        
        checked = [False] * numCourses
        path = [False] * numCourses
        
        for i in range(numCourses):
            if isCyclic(i):
                return False
        
        return True
                    
            