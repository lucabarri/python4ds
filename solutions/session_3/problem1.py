dict1 = {'Person1': 22, 'Person2': 35, 'Person3': 5, 'Person4': 53}
sorted_dict = dict(sorted(dict1.items(), key=lambda elem: elem[1]))
