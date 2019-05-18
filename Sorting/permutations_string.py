from itertools import permutations

data = [''.join(p) for p in permutations('abc')]

print(data)
