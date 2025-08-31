# FCFS with gantt chart:

number = int(input("Number of program: "))

processes = []
for item in range(1, number + 1):
    arrival_time = int(input(f"Enter Arrival Time P{item}: "))
    burst_time = int(input(f"Enter Burst Time P{item}: "))

    pdict = {
        "AT": arrival_time,
        "BT": burst_time,
        "pid": item
    }
    processes.append(pdict)

processes.sort(key=lambda p: p['AT'])  # sort by AT | p = process

current_time = 0
waiting_time = 0
results = []
timeline = []

for process in processes:
    pid = process["pid"]
    AT = process["AT"]
    BT = process["BT"]

    if current_time < AT:
        timeline.append(("IDLE", current_time, AT))
        current_time = AT

    CT = current_time + BT
    TAT = CT - AT
    WT = TAT - BT

    waiting_time += WT

    results.append({
        "PID": pid,
        "AT": AT,
        "BT": BT,
        "CT": CT,
        "TAT": TAT,
        "WT": WT
    })
    timeline.append((pid, current_time, CT))
    current_time = CT

for result in results:
    print(f"Process: P{result.get('PID')}, AT: {result.get('AT')}, "
          f"{result.get('BT')}, {result.get('CT')}, {result.get('TAT')}, {result.get('WT')}")

print(f"Average Waiting time: {waiting_time / number}")

print("Gantt Chart:")
for label, s, e in timeline:
    print(f"[{s}]--P{label}--[{e}]", end=" ")
