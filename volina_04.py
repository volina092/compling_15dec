num = int(input('введи число: '))
log = 0
while 2 ** log <= num:
    print(2 ** log)
    log += 1
