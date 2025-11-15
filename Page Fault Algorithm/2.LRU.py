# Page_Fault (LRU):

def LRU(processes, frame_size):

    table=[["-" for _ in range(frame_size)]for i in range(len(processes))]

    page_fault = 0
    last_used = {}

    for i,p in enumerate(processes):
        if i:
            table[i]=table[i-1].copy()

        if p in table[i]:
            last_used[p] = i
            continue

        page_fault += 1

        if "-" in table[i]:
            j=table[i].index("-")

        else:
            j=min(range(frame_size),key=lambda x:last_used.get(table[i][x],-1))

        table[i][j] = p
        last_used[p] = i

    print("LRU page replacement")
    print("Page_Faults :",page_fault)
    for r in table:
        print(r)

processes=list(map(int,input("Enter processes: ").split()))
frame_size=int(input("Enter frame size: "))
LRU(processes,frame_size)