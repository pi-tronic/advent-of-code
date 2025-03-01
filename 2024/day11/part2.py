from time import time

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readline().split(' ')

def rules(k, number):
    if k==0:
        return number
    # rule 1: value is 0 -> becomes 1
    else:
        if number=='0':
            if k >= 4:
                res0 = rules(k-4, '2')
                res1 = rules(k-4, '0')
                res3 = rules(k-4, '4')
                res = ' '.join([res0, res1, res0, res3])
            else:
                res = rules(k-1, '1')
        elif number=='1' and k >= 3:
            res0 = rules(k-3, '2')
            res1 = rules(k-3, '0')
            res3 = rules(k-3, '4')
            res = ' '.join([res0, res1, res0, res3])
        elif number=='1' and k >= 3:
            res0 = rules(k-3, '4')
            res1 = rules(k-3, '0')
            res3 = rules(k-3, '8')
            res = ' '.join([res0, res1, res0, res3])
        elif number=='1' and k >= 3:
            res0 = rules(k-3, '6')
            res1 = rules(k-3, '0')
            res2 = rules(k-3, '7')
            res3 = rules(k-3, '2')
            res = ' '.join([res0, res1, res2, res3])
        elif number=='1' and k >= 3:
            res0 = rules(k-3, '8')
            res1 = rules(k-3, '0')
            res2 = rules(k-3, '9')
            res3 = rules(k-3, '6')
            res = ' '.join([res0, res1, res2, res3])
        elif number=='1' and k >= 5:
            res0 = rules(k-5, '2')
            res1 = rules(k-5, '0')
            res2 = rules(k-5, '4')
            res3 = rules(k-5, '8')
            res = ' '.join([res0, res1, res2, res3, res0, res3, res3, res1])
        elif number=='1' and k >= 5:
            res0 = rules(k-5, '2')
            res1 = rules(k-5, '4')
            res2 = rules(k-5, '5')
            res3 = rules(k-5, '6')
            res4 = rules(k-5, '7')
            res5 = rules(k-5, '9')
            res = ' '.join([res0, res1, res2, res4, res5, res1, res2, res3])
        elif number=='1' and k >= 5:
            res0 = rules(k-5, '0')
            res1 = rules(k-5, '2')
            res2 = rules(k-5, '3')
            res3 = rules(k-5, '6')
            res4 = rules(k-5, '7')
            res5 = rules(k-5, '8')
            res = ' '.join([res1, res5, res3, res4, res3, res0, res2, res1])
        elif number=='1' and k >= 5:
            res0 = rules(k-5, '1')
            res1 = rules(k-5, '3')
            res2 = rules(k-5, '4')
            res3 = rules(k-5, '6')
            res4 = rules(k-5, '8')
            res5 = rules(k-5, '9')
            res = ' '.join([res1, res3, res4, res3, res5, res0, res4, res2])
        # rule 2: lenght of value is even -> two stones
        elif not len(number) % 2:
            res0 = rules(k-1, str(int(number[:int(len(number)/2)])))
            res1 = rules(k-1, str(int(number[int(len(number)/2):])))
            res = res0 + ' ' + res1
        # rule 3: all other cases -> multiply by 2024
        else:
            res = rules(k-1, str(int(number) * 2024))
    return res

numbers = []
for number in contents:
    if number not in numbers:
        numbers.append(number)
numbers = [numbers[0]]
total = 0
for number in numbers:
    time0 = time()
    total += len(rules(40, number).split(' '))
    time1 = time()
    print(f"{number} : {time1-time0}")

print(total)