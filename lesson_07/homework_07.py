# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while  number * multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum(a,b):
    result = a+b
    return result


print(sum(3,5))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(numbers):
    length = len(numbers)
    result = sum(numbers)/length
    return result


print(average([3, 333, 7]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(string):
    result = string[::-1]
    return result


print(reverse_string('Hello Word'))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def max_word(words):
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(max_word(['Hellllllllo', 'Word',  'Annnnnnnnnnnnnnnnnnnnna']))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

def find_second_tom_position(adwentures_of_tom_sawer):

    adwentures = adwentures_of_tom_sawer.split()

    counter = 0

    for i, word in enumerate(adwentures):
        if word == "Tom":
            counter = counter + 1

            if counter == 2:
                return (i)



find_second_tom_position(adwentures_of_tom_sawer)



# task 8

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""



def find_all_pages(total_foto):
    pages = 8
    total_page = total_foto // pages
    print(total_page)


find_all_pages(232)


# task 9

# task 02 == Виправте синтаксичні помилки


def greet():
    hello = "Hello"
    world = "world"
    return f"{hello} {world}!"

print(greet())

# task 10

"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-й

ний бак?
"""
import math

def total_all_fuel(distance,fuel_per_100km):
    total_fuel = distance * fuel_per_100km / 100
    return total_fuel

print(total_all_fuel(1600,9))

def refuels(tank_volume, total_fuel):
    refuels = math.ceil(total_fuel / tank_volume)
    return refuels

total = total_all_fuel(1600,9)
print(refuels(total, 48))






"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""