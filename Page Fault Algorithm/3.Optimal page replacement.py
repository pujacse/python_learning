# Page_Fault (OPT):

def OPT(processes, frame_size):

    table=[["-" for i in range(frame_size)]for i in range(len(processes))]

    page_fault = 0

    for i in range(len(processes)):
        process = processes[i]

        if i >= 1:
            table[i] = list(table[i-1])

        if process in table[i]:
            continue

        page_fault += 1

        if "-" in table[i]:
            j = table[i].index("-")
        else:
            future = processes[i+1:]

            def next_use(page):
                return future.index(page)+1 if page in future else float('inf')

            j = max(range(frame_size), key = lambda x:next_use(table[i][x]))

        table[i][j] = process

    print("OPT page replacement")
    print("Page_Faults :",page_fault)
    for i in table:
        print(i)

processes=list(map(int,input("Enter processes: ").split()))
frame_size=int(input("Enter frame size: "))
OPT(processes,frame_size)