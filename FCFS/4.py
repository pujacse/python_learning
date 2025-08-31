# FCFS:

number = int(input("Number of process: "))

itemlist = []

for item in range(1,number+1):
    arrival_time = int(input("Enter arrival time: "))
    burst_time = int(input("Enter burst time: "))

    numdict = {
        "PID" : item,
        "AT" : arrival_time,
        "BT" : burst_time
    }
    itemlist.append(numdict)

itemlist.sort(key = lambda p: p["AT"])

current_time = 0
waiting_time = 0
results = []

for item in itemlist:
    pid = item["PID"]
    AT = item["AT"]
    BT = item["BT"]

    if current_time < AT:
        current_time = AT

    CT = current_time + BT
    TAT = CT - AT
    WT = TAT - BT

    waiting_time += WT

    results.append({
        "PID" : pid,
        "AT" : AT,
        "BT" : BT,
        "CT" : CT,
        "TAT" : TAT,
        "WT" : WT
    })

for result in results:
    print(f"process: p{result.get('PID')},{result.get('AT')}")

print(f"Average waiting time: {waiting_time / number}")