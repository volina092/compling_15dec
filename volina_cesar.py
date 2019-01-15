arr = []
eng = 'abcdefghijklmnopqrstuvwxyz'
rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in input().lower():
    if i in eng:
        arr.append(eng[(eng.index(i) + 1) % len(eng)])
    if i in rus:
        arr.append(rus[(rus.index(i) + 1) % len(rus)])
print(''.join(arr))