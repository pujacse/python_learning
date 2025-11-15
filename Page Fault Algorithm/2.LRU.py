# Page_Fault (LRU):

def LRU(processes, frame_size):

    table=[["_" for _ in range(frame_size)]for i in range(len(processes))]

    page_fault = 0
    last_used = {}

    for i,process in enumerate(processes):
        # i for index and p for page number

        if i >= 1:
            # means-if != 0 (0 holei false)
            table[i] = list(table[i-1])

        if process in table[i]:
            # So, jodi page already thake frame e,
            # kichu replace/insert korbo na,
            # sudhu last use time update korbo.
            last_used[process] = i
            continue

        page_fault += 1

        if "-" in table[i]:
            # j means oi slot number
            j=table[i].index("-")

        else:
            # ei line valo kore bujhte hobe. ami bujhi nai
            # ei line ta.
            j=min(range(frame_size),key=lambda x:last_used.get(table[i][x],-1))

        table[i][j] = process
        # current row e, j no. slot e notun page p boshalam.
        last_used[process] = i

    print("LRU page replacement")
    print("Page_Faults :",page_fault)
    for i in table:
        print(i)

processes=list(map(int,input("Enter processes: ").split()))
frame_size=int(input("Enter frame size: "))
LRU(processes,frame_size)