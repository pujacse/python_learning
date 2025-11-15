t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    initial_chemicals = list(map(int, input().split()))
    chemicals = set(initial_chemicals)
    reactions = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        reactions.append((x, y, z))

    changed = True
    while changed:
        changed = False
        for x, y, z in reactions:
            if x in chemicals and y in chemicals and z not in chemicals:
                chemicals.add(z)
                changed = True

    print(len(chemicals))
