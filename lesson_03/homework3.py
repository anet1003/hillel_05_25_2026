alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = """'"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n"'
                       'I don't much care where - " said Alice.\n"'
                       'Then it doesn't matter which way you go," said the Cat.\n"
                       '- so long as I get somewhere," Alice added as an explanation.\n"'
                       'Oh, you're sure to do that," said the Cat, "if you only walk long enough."'"""

symbol = "'"
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)


print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""


black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Сума Чорного та Азовського морів: {total_area}км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

sum_of_all_warehouses = 375291
warehouse_1_warehouse_2 = 250449
warehouse_2_warehouse_3  = 222950

warehouse_3 = sum_of_all_warehouses - warehouse_1_warehouse_2
warehouse_1 = sum_of_all_warehouses - warehouse_2_warehouse_3
warehouse_2 = warehouse_1_warehouse_2 - warehouse_1

print(warehouse_1, warehouse_2, warehouse_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

period_of_payment = 18
month_cost = 1179

total_cost = 1179*18
print(f"Повна вартість комп’ютера: {total_cost}грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print("a)",8019 % 8)
print("b)",9907 % 9)
print("c)",2789 % 5)
print("d)",7248 % 6)
print("e)",7128 % 5)
print("f)",19224 % 9)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza = 274
small_pizza = 218
sik = 35
cake = 350
water = 21

total_cost = big_pizza * 4 + small_pizza * 2 + sik * 4 + water * 3 + cake
print(total_cost)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_foto = 232
pages = 8
total_page = total_foto // pages
print(total_page)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
tank_volume = 48
fuel_per_100km = 9

total_fuel = distance * fuel_per_100km / 100
print(f"Потрібно бензину: {total_fuel} л")

refuels = round(int(total_fuel / tank_volume))
print(f"Мінімальна кількість заправок: {refuels}")

