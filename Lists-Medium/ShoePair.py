n = ['7L', '7R', '7L', '8L', '6R', '7R', '8R', '6R']

shoes = n   # already a list

count = {}

for shoe in shoes:
    size = shoe[:-1]
    side = shoe[-1]

    if size not in count:
        count[size] = {'L': 0, 'R': 0}

    count[size][side] += 1

pairs = 0
for size in count:
    pairs += min(count[size]['L'], count[size]['R'])

print(pairs)