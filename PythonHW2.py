# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

print('Input a number: ', end='')
n = input()
number = list(n)
for i in number:
    if i == '.':
        number.remove('.')
        break
if (number[0] == '-'):
    negative = number.pop((0))
    number[0] = negative + number[0]
sum = 0
for i in number:
    sum = sum + int(i)
print(f'Sum of digits: {sum}')
        
# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Input a number: ', end='')
while True:
    try: 
        number = int(input())
        break
    except: print('It is not an integer number!')
multNums = []
mult = 1
if number == 0:
        multNums.append(1)
else:
    for i in range(1, number + 1):
        mult *= i
        multNums.append(mult)
print(multNums)

# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

print('Input a number: ', end='')
while True:
    try: 
        polindrom = int(input())
        break
    except: print('It is not a number!')
def ReverseOrder(x):
    xReversed = 0
    while(x > 0):
        ost = x % 10
        x = x // 10
        xReversed = xReversed * 10
        xReversed = xReversed + ost
    return xReversed
polindromReversed = ReverseOrder(polindrom)
def CalculatePolindrome(polindrom, polindromReversed):
    if polindrom == polindromReversed:
        return polindrom
    else:
        while (polindromReversed != polindrom):
            polindromReversed = polindromReversed + polindrom
            polindrom = ReverseOrder(polindromReversed)
        return polindromReversed
print(f'Polindrome of {polindrom} is: {CalculatePolindrome(polindrom, polindromReversed)}')

# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time
print('Input min range: ', end='')
while True:
    try: 
        minRange = int(input())
        break
    except:
        print('Invalid number!')
        print('Input min range: ', end='')
print('Input max range: ', end='')
while True:
    try: 
        maxRange = int(input())
        break
    except: 
        print('Invalid number!')
        print('Input min range: ', end='')
if minRange < maxRange:
    s = time.time_ns()
    calc = maxRange - minRange
    dif = (s//100) % 10
    if calc == 1:
        print(f'A random number from range is: {minRange + round(calc * (0.1 * dif))}')
    else:
        print(f'A random number from range is: {minRange + round(calc * (0.1 * dif))}')
else: print('minRange needs to be smaller than maxRange!')