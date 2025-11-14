# FIFO page replacement algorithm:
# processes = [2, 1, 3, 6, 4]

def FIFO(processes,frame_size):

    # table make:
    table = [["-" for _ in range(frame_size)] for i in range(len(processes))]

    replace = 0
    page_fault = 0

    # i for index = 0
    for i in range(len(processes)):
        process = processes[i] # process = 2

        # if same value is available in the table, copy previous values
        if i >= 1:
            table[i] = list(table[i-1])

        # if same value is not in table, increase page_fault and replace the first value place
        if process not in table[i]:
            page_fault += 1
            table[i][replace] = process

            # increase our pointer
            # circular pointer
            replace = (replace + 1) % frame_size

    print("Page fault algorithm")
    print("Page_faults : ", page_fault)
    # print the overall values
    for i in table:
        print(i)

processes = list(map(int,input("Enter processes: ").split()))
frame_size = int(input("Enter frame_size: "))
FIFO(processes, frame_size)