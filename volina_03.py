word = input()
if word[0] not in ['а', 'е', 'э', 'я']:
    word = word[::-1]
for i in word:
    print(i)