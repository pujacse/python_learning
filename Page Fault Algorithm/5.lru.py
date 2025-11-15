# Page_Fault (LRU):

def LRU(processes, frame_size):

    table = [["-" for _ in range(frame_size)] for i in range(len(processes))]

    # replace pointer (FIFO এ ছিল) আর দরকার নেই; LRU এ আমরা last_used টাইমস্টাম্প রাখব
    last_used = [-1] * frame_size  # প্রতিটি ফ্রেমে শেষ কবে ব্যবহার হয়েছে (time index i)
    page_fault = 0

    for i in range(len(processes)):
        process = processes[i]

        # copy previous alignment (same যেমন আগে ছিল)
        if i >= 1:
            table[i] = list(table[i-1])

        # যদি পেজটি ফ্রেমে থাকে → hit: তার last_used আপডেট করো
        if process in table[i]:
            idx = table[i].index(process)
            last_used[idx] = i  # এখন এটি সর্বশেষ i তে ব্যবহার হয়েছে
        else:
            page_fault += 1

            # প্রথমে খালি স্লট আছে কিনা দেখো ("-" আছে)
            if "-" in table[i]:
                idx = table[i].index("-")  # প্রথম খালি স্লট
                table[i][idx] = process
                last_used[idx] = i
            else:
                # কোন ফ্রেমটি সবচেয়ে আগে ব্যবহার হয়েছে? (LRU -> min last_used)
                lru_index = min(range(frame_size), key=lambda x: last_used[x])
                table[i][lru_index] = process
                last_used[lru_index] = i

    print("LRU page replacement")
    print("Page_Faults : ", page_fault)
    for row in table:
        print(row)

processes = list(map(int, input("Enter processes: ").split()))
frame_size = int(input("Enter frame size: "))
LRU(processes, frame_size)
