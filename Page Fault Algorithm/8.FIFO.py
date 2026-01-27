# Page_Fault (FIFO):

def FIFO(processes, frame_size):

    table = [["-" for _ in range(frame_size)] for i in range(len(processes))]

    replace = 0
    page_fault = 0

    for i in range (len(processes)):
        process = processes[i]

        if i >= 1:
            table[i] = list(table[i-1])

        if process not in table[i]:
            # in FIFO, we replace with the replacement pointer
            page_fault += 1
            table[i][replace] = process

            replace = (replace+1) % frame_size

    print("FIFO page replacement")
    print("Page_Faults : ",page_fault)
    for i in table:
        print(i)

processes=list(map(int,input("Enter processes: ").split()))
frame_size=int(input("Enter frame size: "))
FIFO(processes,frame_size)