# Zadania 2.10-2.19
# 2.10
print('2.10')
line = """Lorem ipsum dolor sit amet
Morbi\tcongue dictum pellentesque\tdolor
Nullam eget rutrum tortor
GvR"""
print(line)
print(f'Liczba wyrazów w line: {len(line.split())}')

# 2.11
print('\n2.11')
print('_'.join('word'))

# 2.12
print('\n2.12')
pierwsze_znaki_wyrazow = "".join(word[0] for word in line.split())
print(pierwsze_znaki_wyrazow)
ostatnie_znaki_wyrazow = "".join(word[-1] for word in line.split())
print(ostatnie_znaki_wyrazow)

# 2.13
print('\n2.13')
print(sum(len(word) for word in line.split()))

# 2.14
print('\n2.14')
# a
longest_word = max(line.split(), key=len)
print(longest_word)
# b
longest_word_length = len(longest_word)
print(longest_word_length)

# 2.15
print('\n2.15')
L = [4, 5, 3, 6, 7, 10, 12, 2, 1, 4, 3, 2]
L_str = [str(i) for i in L]
s = "".join(L_str)
print(s)

# 2.16
print('\n2.16')
s = line.replace('GvR', 'Guido van Rossum')
print(s)

# 2.17
print('\n2.17')
words_in_line = line.split()
print(words_in_line)
alphabetically_sorted = sorted(words_in_line)
print(alphabetically_sorted)
sorted_by_length = sorted(words_in_line, key=len, reverse=True)
print(sorted_by_length)

# 2.18
print('\n2.18')
integer_val = 123040302440213000
zero_count = str(integer_val).count('0')
print(zero_count)

# 2.19
print('\n2.19')
L = [1, 4, 6, 12, 24, 67, 89, 102, 120, 250, 650, 980]
print(L)
L_with_three_digits = [str(i).zfill(3) for i in L]
print(L_with_three_digits)
