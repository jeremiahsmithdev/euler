def divisors(number):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count = count + 1
    return count


print(divisors(50000000))

# notfound = True
# current = 1
# while notfound:
#     print(current)
#     if divisors(current) > 500:
#         notfound = False
#         print(current)
#     current = current + 1





