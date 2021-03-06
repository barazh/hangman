from random import *


def get_word():  # Возвращает случайное слово из списка в верхнем регистре
    word = choice(words_list).upper()
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  ---
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                  ---
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                  ---
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                  ---
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                '''
    ]
    return stages[tries]


def play(word, difficulty):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    tmp_word = word

    print()
    print("Давайте играть в угадайку слов!")

    if difficulty == '1':
        word_completion = word[0] + word_completion[1:len(word) - 1] + word[-1]


    print(display_hangman(tries))
    print(f'Загаданно слово {word_completion} из {len(word)} букв')

    while True:
        if tries == 0:
            print(f'У вас закончились попытки! Было загаданно слово {word}')
            break
        elif word_completion == word:
            print(f'Поздравляем, вы угадали слово! Вы победили!')
            break

        word_in = input('Введите букву или слово: ').strip().upper()

        if not word_in.isalpha():  # Проверяем входный ввод. Пропукает только буквы
            print("Пожалуйста, введите коректное значение!")
            continue
        elif len(word_in) == 1 and word_in in guessed_letters:  # Проверяем наличие ранее названных букв
            print(f'Вы уже называли букву {word_in}, попробуйте другую.')
            continue
        elif len(word_in) == len(word) and word_in in guessed_words:  # Проверяем наличие ранее названных слов
            print(f'Вы уже называли слово {word_in}, попробуйте другое.')
            continue
        elif len(word_in) != len(word) and len(word_in) != 1:  # Проверка если ввести слово другой длины
            print(f'Введенное вами слово отличается по длине от загадонного.')
            continue

        if word_in == word:  # Если пользователь ввел правильное слово
            print('Поздравляем, вы угадали слово! Вы победили!')
            break
        elif word_in != word and len(word_in) > 1:  # Если пользователь ввел НЕ правильное слово
            print("Вы не угадали слово!")
            guessed_words.append(word_in)
            tries -= 1
            print(display_hangman(tries))
            print(word_completion)
            continue
        elif word_in not in word and len(word_in) == 1:  # Если пользователь ввел НЕ правильную букву
            print('Такой бквы нет!')
            guessed_letters.append(word_in)
            tries -= 1
            print(display_hangman(tries))
            print(word_completion)
            continue
        elif word_in in word and len(word_in) == 1:  # Если пользователь угадал букву
            print('Есть такая буква!')
            guessed_letters.append(word_in)
            for _ in range(word.count(word_in)):
                word_completion = word_completion[:tmp_word.find(word_in)] + word_in + word_completion[tmp_word.find(word_in) + 1:]
                tmp_word = tmp_word.replace(word_in, "_", 1)
            print(word_completion)
            continue


words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
              "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница",
              "магазин", "председатель", "сотрудник", "республика", "личность"]

while True:
    while True:
        difficulty = input('Выбирите уровень сложности игры. 1 - Легкий, 2 - Нормальный: ')
        if difficulty == '1' or difficulty == '2':
            break
        else:
            print('Введите коректное значение!')
            continue

    play(get_word(), difficulty)
    print()
    user_otvet = int(input("Хотите повторить игру? Введите 1 если Да, или 2 если Нет: "))
    if user_otvet == 1:
        continue
    else:
        break
