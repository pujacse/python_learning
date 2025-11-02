# Page_Fault :

# [0,3,1,2,4,1,2,3,0,4]
# Frame_size = 3


def FIFO(processes, frame_size):

    tracker = [["-" for _ in range(frame_size)] for i in range(len(processes))]

    # pointer to check where to replace

    replace = 0
    page_fault = 0

    for i in range (len(processes)):
        process = processes[i]

        # copy the previous alignment
        if i >= 1:
            tracker[i] = list(tracker[i-1])

        if process not in tracker[i]:
            # in FIFO, we replace with the replacement pointer
            page_fault += 1
            tracker[i][replace] = process

            # increase our pointer
            # circular pointer
            replace = (replace+1) % frame_size

    # that's it
    print("FIFO page replacement")
    print("Page_Faults : ",page_fault)
    for i in tracker:
        print(i)

if __name__ == "__main__":
    processes = [0,3,1,2,4,1,2,3,0,4]
    frame_size = 3
    FIFO(processes, frame_size)