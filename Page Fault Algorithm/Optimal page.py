# optimal page replacement algorithm

def OPT(processes, frame_size):

    table = [["_" for i in range(frame_size)] for i in range(len(processes))]

    page_fault = 0

    for