# Least recently used algorithm:

def LRU(processes, frame_size):
    table = [["_" for i in range(processes)] for i in range(len(processes))]

    for i in range(len(processes)):
        process = processes[i]

        if i >= 1:
            table[i] = list(table[i-1])
            table[i] = map(list[i-1])

        if i not in table[i]:
