# FCFS practice:

number = int(input("Enter process number: "))

itemlist = []
for item in range(1, number+1):
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
results = []
Waiting_time = 0

for item in itemlist:
    pid = item["PID"]
    AT = item["AT"]
    BT = item["BT"]

    if current_time < AT:
        current_time = AT

    CT = current_time + BT
    TAT = CT - AT
    WT = TAT - BT

    Waiting_time += WT

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
    print(f"process: P{result.get('PID')},AT: {result.get('AT')},BT: {result.get('BT')},"
          f"CT: {result.get('CT')},TAT: {result.get('TAT')},WT: {result.get('WT')}")

print(f"average waiting time: {Waiting_time/number}")