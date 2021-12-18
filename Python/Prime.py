import pprint

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_gaps(primes: list) -> dict:
    gaps = {}

    for n in range(2, len(primes)):
        gapsize = primes[n] - primes[n-1]
        gapsize_str = str(gapsize)
        gaps.update({gapsize_str : gaps.setdefault(gapsize_str, 0) + 1})

    return gaps

primes = []

for n in range(2, 10000, 1):
    if is_prime(n):
        primes.append(n)

gaps = prime_gaps(primes)

print(len(primes))
print(primes[0])
print(primes[-1])

print("gaps:", gaps)

with open('.\gaps.txt', 'w') as gaps_file:
    gaps_file.write('Bacon is not a vegetable.')


with open('gaps.py', 'w') as file_obj:
    file_obj.write('gaps = {}\n'.format(pprint.pformat(gaps)))