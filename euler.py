longest = 0
for n in range(1000000):
    term = 0
    terms = 1
    thisn = n
    while n > 1:
        if n % 2 == 0:
            term = n / 2
            terms += 1
        if n % 2 == 1:
            term = 3 * n + 1
            terms += 1
        n = term
    if terms > longest:
        answer = thisn
print answer
