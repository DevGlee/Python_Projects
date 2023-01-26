##############  LOOPS #############


primes = [2, 3, 5, 7]

for prime in primes:

    print(prime)
for x in range(5):

    print(x)


for x in range(3, 6):

    print(x)

for x in range(1, 10, 7):

    print(x)


count = 0

# while count < 5:
# print(count)
# count += 1


while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
    