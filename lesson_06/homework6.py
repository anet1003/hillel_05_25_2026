"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()"""

text = input("Enter text: ")
unique_text = set(text)
length_text = len(unique_text) > 10

print(length_text)