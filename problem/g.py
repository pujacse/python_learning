import sys


def solve():
    try:
        line = sys.stdin.readline().split()
        if not line: return
        N, M = map(int, line)
    except:
        return

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    R = [0] * N
    C = [0] * M

    for i in range(N):
        for j in range(M):
            R[i] ^= matrix[i][j]
            C[j] ^= matrix[i][j]

    initial_S = sum(R) + sum(C)
    min_S = initial_S

    for i in range(N):
        for j in range(M):
            # S' = S - R_i - C_j + (R_i ^ C_j)
            potential_S = initial_S - R[i] - C[j] + (R[i] ^ C[j])
            if potential_S < min_S:
                min_S = potential_S

    print(min_S)


def main():
    try:
        T = int(sys.stdin.readline())
    except:
        T = 0

    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()