# Найти все числа от 1 до 1000, которые делятся на 7

divisible = [x for x in range(1, 1001) if x % 7 == 0]

# Сгенерировать список на основе чисел от 1 до 1000. Если число делится на 3 - положить результат деления в коллецию без изменений, в противном случае положить число записанное дважды друг за другом

result = [i // 3 if i % 3 == 0 else int(str(i) * 2) for i in range(1, 1001)]

# Посчитать кол-во пробелов в строке "  hel l o      world   "

spaces = len([char for char in "  hel l o      world   " if char == ' '])

# Сгенерировать список из слов строки “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”, которые начинаются на Y/y

words_starting_with_y = [word.lower() for word in
                         "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams".split()
                         if word.lower().startswith('y')]

# Для каждого элемента строки  "hi, 3.44, 535  " сгенерировать коллекцию кортежей вида (индекс and значение)

tuple_list = "hi, 3.44, 535  "
result = [(index, char) for index, char in enumerate(tuple_list)]

# Сгенерировать коллекцию с числами из строки "In 1984 there were 13 instances of a protest with over 1000 people attending"

numbers = ["1984", "13", "1000"]
num_list = [int(num.strip()) for line in numbers for num in line.split(' ')]

# Для чисел из промежутка [1, 20] сгенерировать коллекцию строк вида ("четное", "нечетное", "четное")

result = ['even' if n % 2 == 0 else 'odd' for n in range(20)]

# Найти все слова из строки, длина которых меньше 4 символов "The trickiest part of learning list comprehension for me was really understanding the syntax."

word = "The trickiest part of learning list comprehension for me was really understanding the syntax."
result = [word for word in word.split() if len(word) < 4]

# Найти простые числа из промежутка [1, 50]. Простым числом называется число, которое делится только на единицу и на себя же.

result = [x for x in range(2, 50) if all(x % y != 0 for y in range(2, x))]
