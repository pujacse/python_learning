# FCFS:

number = int(input("number of process : "))

processes = []

for pid in range (1, number+1):
    Arrival_time = int(input(f"Enter arrival time p{pid} : "))
    Burst_time = int(input(f"Enter burst time p{pid} : "))

    pdict = {
        "AT" : Arrival_time,
        "BT" : Burst_time,
        "pid" : pid
    }
    processes.append(pdict)

processes.sort(key = lambda p : p['AT'])

current_time = 0
waiting_time = 0
results = []

for process in processes:
    AT = process["AT"]
    BT = process["BT"]
    pid = process["pid"]

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

for result in results :
    print(f"process : p{result.get('PID')}, AT : {result.get('AT')},"
          f"BT : {result.get('BT')}, CT : {result.get('CT')}, TAT : {result.get('TAT')}, WT : {result.get('WT')}")

print(f"Average waiting time : {waiting_time/number}")