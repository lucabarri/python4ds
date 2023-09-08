n = 10

pascal_triangle = [[1, ]]

for i in range(n - 1):
    last_list = pascal_triangle[-1]
    padded_list = [0] + last_list + [0]
    new_list = []
    for val1, val2 in zip(padded_list[:-1], padded_list[1:]):
        new_list.append(val1 + val2)
    pascal_triangle.append(new_list)

for sub_list in pascal_triangle:
    print(sub_list)
