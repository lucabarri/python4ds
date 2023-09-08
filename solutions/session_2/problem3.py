n = 15
n_it = [n]
n_iter = 0

print(n)
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1

    n_iter += 1
    n_it.append(n)
print(f"List of iterates: {n_it}")
print(f"Number of steps: {n_iter}")
