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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

h_count = adwentures_of_tom_sawer.count("h")
print(h_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

adwentures = adwentures_of_tom_sawer.split()

counter = 0

for word in adwentures:
    if word[0].isupper():
        counter = counter + 1

print(counter)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

adwentures = adwentures_of_tom_sawer.split()

counter = 0

for i, word in enumerate(adwentures):
    if word == "Tom":
        counter = counter + 1

        if counter == 2:
            print(i)
            break



# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom = adwentures_of_tom_sawer.replace("....", " ")
adwentures = adwentures_of_tom.split(".")

sentences = []

for sentence in adwentures:
    clean_sentence = " ".join(sentence.split())
    if clean_sentence:
        sentences.append(clean_sentence)

print(sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

adwentures = [
    " ".join(sentence.split())
    for sentence in adwentures_of_tom_sawer.replace("....", " ").split(".")
    if sentence.strip()
]

sentence = adwentures[3].lower()
print(sentence)



# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

adwentures = [
    " ".join(sentence.split())
    for sentence in adwentures_of_tom_sawer.replace("....", " ").split(".")
    if sentence.strip()
]

found = False

for sentence in adwentures:
    if sentence.startswith("By the time"):
        found = True
        break

print(found)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures = [
    " ".join(sentence.split())
    for sentence in adwentures_of_tom_sawer.replace("....", " ").split(".")
    if sentence.strip()
]

last_sentence = adwentures[-1]
word_count = len(last_sentence.split())

print(word_count)



