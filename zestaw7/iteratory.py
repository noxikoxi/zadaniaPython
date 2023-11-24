import itertools
import random

# Zadanie 7.6
# a) Iterator zwracający 0, 1, 0, 1, 0, 1, ...
print("a)\n")
it = itertools.cycle([0, 1])

for i in range(10):
    print(next(it))


# b) iterator zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
class RandomIter:

    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        return self()

    def __call__(self):
        return random.choice(self.sequence)


it2 = RandomIter(["N", "E", "S", "W"])

print("\nb)\n")
for i in range(10):
    print(next(it2))

# c) iterator zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
print("\nc)\n")
it3 = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

for i in range(15):
    print(next(it3))
