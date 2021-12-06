class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []

        intervals = collections.deque(sorted(intervals))
        tmp = intervals.popleft()
        
        while intervals:
            interval = intervals.popleft()
            if tmp[1] >= interval[0] and tmp[1] <= interval[1]:                
                tmp[1] = interval[1]
            elif tmp[1] > (interval[0] and interval[1]):
                continue
            else:
                answer.append(tmp)
                tmp = interval
        
        if answer:
            if answer[-1][1] < tmp[0]:
                answer.append(tmp)
        else:
            answer.append(tmp)
            
        return answer