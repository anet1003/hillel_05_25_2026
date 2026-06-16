"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""

lst = [3, 6, 7, 9, 6, 8, 8, 2, 3, 4, 65, 4,88]

total = 0

for item in lst:
    if item % 2 == 0:
        total = total + item


print(total)