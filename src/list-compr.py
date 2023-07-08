
dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

odd = {key: num for (key, num) in dictionary.items() if num % 2 == 1}
print(odd)
