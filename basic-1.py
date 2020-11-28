import time
start_time = time.time()  # 측정시작


def knapsack(self, w, v, k):
    n = len(w)
    X = [[0 for y in range(k + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for t in range(k + 1):
            if i == 0 or t == 0:
                X[i][t] = 0
            elif w[i-1] <= t:
                X[i][t] = max(v[i-1]
                              + X[i-1][t-w[i-1]],
                              X[i-1][t])
            else:
                X[i][t] = X[i-1][t]

    return X[n][k]


w = [10, 20, 30]
v = [60, 100, 120]
k = 50

print(knapsack(0, w, v, k))


end_time = time.time()  # 측정종료
print("time: ", end_time - start_time)
