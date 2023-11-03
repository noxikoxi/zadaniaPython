# zadanie 4.2
print('\n4.2\n')


def make_ruler(n):
    miarka = "....".join('|' * (n + 1))
    etykiety = '0' + "".join(str(i + 1).rjust(5) for i in range(n))

    return miarka + "\n" + etykiety


def make_grid(rows, cols):
    """
    :param rows: liczba poziomych lini przecinających
    :param cols: liczba pionowych lini przecinających
    :return: siatka o wymiarach rows x cols
    """
    row1 = '+' + '---+' * (cols - 1) + '\n'
    row2 = '|' + '|'.rjust(4) * (cols - 1) + '\n'

    return row2.join([row1] * rows)


print(make_ruler(12))

print(make_grid(3, 4))

# zadanie 4.3
print('\n4.3\n')


def factorial(n):
    if n < 2: return 1
    res = 1
    for i in range(2, n + 1):
        res *= i

    return res


print(factorial(3))
print(factorial(4))
print(factorial(5))

# zadanie 4.4
print('\n4.4\n')


# F0 = 0, F1 = 1
def fibonacci(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2

    return fib1


l = [fibonacci(i) for i in range(10)]
print(l)

# zadanie 4.5
print('\n4.5\n')


def odwracanie(L, left, right):
    if left < 0 or right > len(L) - 1 or left > right:
        print("Podano nieprawidłowe indeksy listy")
        return None

    return L[0:left] + L[left:right + 1][::-1] + L[right + 1:]


def odwracanie_rekurencyjnie(L, left, right):
    if left < 0 or right > len(L) - 1:
        print("Podano nieprawidłowe indeksy listy")
        return None

    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjnie(L, left + 1, right - 1)


assert odwracanie([0, 1, 2, 3, 4, 5], 2, 3) == [0, 1, 3, 2, 4, 5]
print(odwracanie([0, 1, 2, 3, 4, 5], 2, 3))
assert odwracanie([0, 1, 2, 3, 4, 5, 6, 7, 8], 4, 6) == [0, 1, 2, 3, 6, 5, 4, 7, 8]
print(odwracanie([0, 1, 2, 3, 4, 5, 6, 7, 8], 4, 6))

L1 = [1, 2, 3, 4, 5, 6, 7]
odwracanie_rekurencyjnie(L1, 1, 4)
assert L1 == [1, 5, 4, 3, 2, 6, 7]
print(L1)

# zadanie 4.6
print('\n4.6\n')


def sum_sequence(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_sequence(item)
        else:
            result += item

    return result


s1 = [1, 2, 3, [4, 5], (1, 1, (1, 2, 3), [])]
s2 = [1, 1, 1, 1, 1, 1, 1, 1, (1, 2, 2, 1), [3]]

assert sum_sequence(s1) == 23
print(sum_sequence(s1))

assert sum_sequence(s2) == 17
print(sum_sequence(s2))

# zadanie 4.7
print('\n4.7\n')
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]


def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += flatten(item)
        else:
            result.append(item)

    return result


assert flatten(seq) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten(seq))
