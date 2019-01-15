word = input('Введи слово!')
for i in range(word(len)):
    if word[1] in ['к', 'и', 'л'] and not i % 2:
        print(word[i])
    elif i % 2:
        print(word[i])