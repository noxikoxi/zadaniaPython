# 3.1
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# Powyższy kod nie jest poprawny składniowo w Pythonie, ponieważ:
# - występują w nim średniki na końcu przypisywania wartości zmiennych
# - pojedyncze wyrażenie x > y nie potrzebuje nawiasów
# - samo przypisanie wartości dla dwóch zmiennych powinno odbyć się w dwóch liniach lub za pomocą: x, y = 2, 3


# for i in "axby": if ord(i) < 100: print (i)

# Powyższy kod nie jest poprawny składniowo, ponieważ:
# - po dwukropku (:) należy zrobić wcięcie w kodzie dla następnych instrukcji

for i in "axby": print(ord(i) if ord(i) < 100 else i)

# Powyższy kod jest poprawny składniowo, ponieważ jest szczególnym przypadkiem wykorzystania
# instrukcji warunkowej if oraz instrukcji prostej, lepiej jednak unikać tego przypadku

# 3.2
# L = [3, 5, 4] ; L = L.sort()
# Metoda sort nie zwraca nic, tylko sortuje zawartość listy, więc po takim przypisaniu L będzie None

# x, y = 1, 2, 3
# Za dużo wartości po prawej stronie przypisania, powinny być tylko dwie

# X = 1, 2, 3 ; X[1] = 4
# Powyższe przypisanie tworzy z X krotkę a jej elementów nie można zmienić

# X = [1, 2, 3] ; X[3] = 4
# W liście X indeks 3 nie występuje, zawiera ona 3 elementy o indeksach 0,1,2

# X = "abc" ; X.append("d")
# X jest stringiem a stringi nie posiadają metody append

# L = list(map(pow, range(8)))
# Funkcja pow wymaga dwóch argumentów a został podany tylko jeden

# 3.3
print("\n3.3\n")
for i in range(0, 31):
    if i % 3 != 0:
        print(i)
# 3.4
print("\n3.4\n")
while True:
    x = input()

    if x == 'stop':
        break

    try:
        x = float(x)
        print(x, pow(x, 3))
    except ValueError:
        print('Błąd, nie wpisano liczby rzeczywistej\nSpróbuj Ponownie')

# 3.5
print("\n3.5\n")
dlugosc = 12
miarka = "|"
etykiety = "0"
for i in range(dlugosc):
    miarka += "....|"
    etykiety += str(i + 1).rjust(5)

miarka = miarka + "\n" + etykiety
print(miarka)

# 3.6
print("\n3.6\n")
nCol = 5  # Liczba kolumn
nRow = 3  # Liczba wierszy
row = '+' + '---+' * (nCol - 1)
prostokat = row

for i in range(nRow - 1):
    prostokat = ''.join([prostokat, '\n|', '|'.rjust(4) * (nCol - 1), '\n', row])

print(prostokat)

# 3.8
print("\n3.8\n")
s1 = [1, 2, 3, 4, 5]
s2 = [4, 5, 6, 7, 8]
s3 = 'abcdef'
s4 = 'defghi'
# a)
print(list(set(s1).intersection(set(s2))))
print(list(set(s3).intersection(set(s4))))

# b)
print(list(set(s1).union(set(s2))))
print(list(set(s3).union(set(s4))))

# 3.9
print("\n3.9\n")
l = [[], [4], (1, 2), [3, 4], (5, 6, 7), (1, 1, 1, 1), [10, 20, 30, 40]]
result = [sum(x) for x in l]
print(result)

# 3.10
print("\n3.10\n")
r_to_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
r_to_int2 = dict(zip(keys, values))
r_to_int3 = {key:value for key, value in zip(keys, values)}

print(r_to_int)
print(r_to_int2)
print(r_to_int3)


def roman2int(roman):
    value = 0
    last_roman_val = 0
    for number in roman[::-1]:
        temp = r_to_int[number]

        if temp < last_roman_val:
            value -= temp
        else:
            value += temp

        last_roman_val = temp
    return value


assert(roman2int('XIV') == 14)
print(roman2int('XIV'))
assert(roman2int('MDC') == 1600)
print(roman2int('MDC'))
assert(roman2int('MMXXIII') == 2023)
print(roman2int('MMXXIII'))
assert(roman2int('MCMXL') == 1940)
print(roman2int('MCMXL'))
