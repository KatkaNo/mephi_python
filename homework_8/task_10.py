strange_word = input()
norm_word = ''
i = 0
k = 0

for letter in strange_word:
    if i % 2 == 0:
        norm_word += letter
    i += 1

for letter in strange_word[::-1]:
    if k % 2 == 0:
        norm_word += letter
    k += 1

print(norm_word)
