numbers = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_numbers(text):
    try:
        numbers_list = text.split(",")
        total = 0

        for number in numbers_list:
            total += int(number)

        return total

    except ValueError:
        return "Не можу це зробити!"


for item in numbers:
    print(sum_numbers(item))
