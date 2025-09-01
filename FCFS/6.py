# FCFS:

number = int(input("Number of process: "))
numlist = []

for item in range(1, number+1):
    arrival_time = int(input("Enter arrival time: "))
    burst_time = int(input("Enter burst time: "))

    numdict = {
        "PID" : item,
        "AT" : arrival_time,
        "BT" : burst_time
    }
    numlist.append(numdict)

numlist.sort(key=lambda p: p['AT'])

current_time = 0
results = []

for item in numlist:
    pid = item["PID"]
    AT = item["AT"]
    BT = item["BT"]

    if current_time < AT:
        current_time = AT

    CT = current_time + BT
    TAT = CT - AT
    WT = TAT - BT

    results.append({
        "PID" : pid,
        "AT" : AT,
        "BT" : BT,
        "CT" : CT,
        "TAT" : TAT,
        "WT" : WT
    })
    current_time = CT

for result in results:
    print(f"Process P{result.get('PID')}, Arrival time: {result.get('AT')}, Burst time: {result.get('BT')},"
          f"Completion time: {result.get('CT')} ,Turn arround time: {result.get('TAT')},"
          f"Waiting time: {result.get('WT')}")