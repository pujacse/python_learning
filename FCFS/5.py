# FCFS:

number = int(input("Number of process: "))

itemlist = []

for item in range(1, number+1):
    arrival_time = int(input("Enter arrival time: "))
    burst_time = int(input("Enter burst time: "))

    item_dict = {
        "PID" : item,
        "AT" : arrival_time,
        "BT" : burst_time
    }
    itemlist.append(item_dict)

itemlist.sort(key=lambda p: p["AT"])

current_time = 0
results = []
waiting_time = 0

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
    current_time = CT

for result in results:
    print(f"Process: P{result.get('PID')}, AT: {result.get('AT')}, "
          f"{result.get('BT')}, {result.get('CT')}, {result.get('TAT')}, {result.get('WT')}")

print(f"Average waiting time: {waiting_time / number}")