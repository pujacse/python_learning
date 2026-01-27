# LRU page replacement algorithm

def LRU(processes, frame_size):

    table = [["_" for i in range(frame_size)] for i in range(len(processes))]

    page_fault = 0
    last_used = {}

    for i in range(len(processes)):
        process = processes[i]

        if i >= 1:
            table[i] = list(table[i-1])

        if process in table[i]:
            last_used[process] = i
            continue
        page_fault += 1

        if "_" in table[i]:
            j = table[i].index("_")

        else:
            j = min(range(frame_size),key=lambda x:last_used.get(table[i][x],-1))

        table[i][j] = process
        last_used[process] = i

    print("LRU page replacement algorithm")
    print("page_fault: ",page_fault)
    for i in table:
        print (i)

processes = list(map(int,input("Enter processes: ").split()))
frame_size = int(input("Enter frame_size: "))
LRU(processes, frame_size)