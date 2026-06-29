n =1530

original = n

lengt = str(n)
lengths = list(lengt)
length =  len(lengths)
total = 0
while n > 0:
    last_digit = n % 10
    total += last_digit**length
    n =  n // 10


if total == original:
    print(True)
else:
    print(False)


