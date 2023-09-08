n = 5
m = 5

S = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        S += (pow(i, 2) * j) / (pow(3, i) * (j * pow(3, i) + i * pow(3, j)))

print(S)
