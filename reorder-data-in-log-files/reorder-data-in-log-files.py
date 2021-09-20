class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            log = log.split()
            content = log[1:]
            if content[0].isdigit():
                digit_logs.append(' '.join(log))
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x: (x[1:], x[0]))
        for i in range(len(letter_logs)):
            letter_logs[i] = ' '.join(letter_logs[i])

        return letter_logs + digit_logs
            