import functools
import time


@functools.lru_cache(maxsize=None)
def squareOfNumber(i):
    time.sleep(2)
    return (i**2)


print("Values will be computed and stored in cache....")
for i in range(0, 5):
    print(f"{i}^2={squareOfNumber(i)}")

print("Values will be printed from cache....")
for i in range(0, 5):
    print(f"{i}^2={squareOfNumber(i)}")
