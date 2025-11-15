# Page_Fault (OPT):

def OPT(processes, frame_size):

    tracker=[["-" for _ in range(frame_size)]for _ in processes]

    page_fault = 0

    for i,p in enumerate(processes):
        if i:
            tracker[i]=tracker[i-1].copy()

        if p in tracker[i]:
            continue

        page_fault += 1

        if "-" in tracker[i]:
            j = tracker[i].index("-")

        else:
            future = processes[i+1:]

            def next_use(page):
                return future.index(page)+1 if page in future else float('inf')

            j = max(range(frame_size), key = lambda x: next_use(tracker[i][x]))

        tracker[i][j] = p

    print("OPT page replacement")
    print("Page_Faults :",page_fault)
    for r in tracker:
        print(r)

processes=list(map(int,input("Enter processes: ").split()))
frame_size=int(input("Enter frame size: "))
OPT(processes,frame_size)