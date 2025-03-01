from time import time

numbers = ['6']


def rules(k, number):
    if k==0:
        return number
    # rule 1: value is 0 -> becomes 1
    else:
        if number=='0':
            res = rules(k-1, '1')
        # rule 2: lenght of value is even -> two stones
        elif not len(number) % 2:
            res0 = rules(k-1, str(int(number[:int(len(number)/2)])))
            res1 = rules(k-1, str(int(number[int(len(number)/2):])))
            res = res0 + ' ' + res1
            global total
            total += 1
        # rule 3: all other cases -> multiply by 2024
        else:
            res = rules(k-1, str(int(number) * 2024))
    return res


for i in range(20):
    total = 0
    for number in numbers:
        total += len(rules(i, number).split(' '))

    print(i, total)