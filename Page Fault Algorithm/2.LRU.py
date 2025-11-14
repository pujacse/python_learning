# Page_Fault (LRU):

def LRU(processes, frame_size):

    tracker=[["-" for _ in range(frame_size)]for _ in processes]

    page_fault = 0
    last = {}

    for i,p in enumerate(processes):
        if i:
            tracker[i]=tracker[i-1].copy()

        if p in tracker[i]:
            last[p] = i
            continue

        page_fault += 1

        if "-" in tracker[i]:
            j=tracker[i].index("-")

        else:
            j=min(range(frame_size),key=lambda x:last.get(tracker[i][x],-1))

        tracker[i][j] = p
        last[p] = i

    print("LRU page replacement")
    print("Page_Faults :",page_fault)
    for r in tracker:
        print(r)

processes=list(map(int,input("Enter processes: ").split()))
frame_size=int(input("Enter frame size: "))
LRU(processes,frame_size)