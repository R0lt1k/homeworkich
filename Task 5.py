import itertools
subsequence = input("Введите последовательность символов: ")

words = []

for length in range(1, len(subsequence) + 1):
    permutations = itertools.permutations(subsequence, length)
    for perm in permutations:
        word = ''.join(perm)
        if word not in words:
            words.append(word)

print("Список слов: ")
for word in words:
    print(word)
print("Количество слов: ", len(words))
