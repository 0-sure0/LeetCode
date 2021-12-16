class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = Counter(tasks)
        
        max_task_count = max(tasks_count.values())
        num_max_tasks = list(tasks_count.values()).count(max_task_count)
        return max((max_task_count - 1) * (n + 1) + num_max_tasks, len(tasks))