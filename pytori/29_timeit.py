import timeit
one = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
two = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
three = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f"1: {one}, 2: {two}, 3: {three}")