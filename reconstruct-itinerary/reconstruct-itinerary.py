class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:        
        travel = collections.defaultdict(list)
        answer = []
        
        for depart, dest in sorted(tickets):
            travel[depart].append(dest)
        
        def dfs(depart):
            while travel[depart]:
                dfs(travel[depart].pop(0))
            answer.append(depart)
        
        dfs('JFK')        
        return answer[::-1]
        
        
            
        
        