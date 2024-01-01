from  colorama import init, Fore
import random
init(convert=True)
print('Приветствую тебя, дорогой друг!', 'Ты запустил игру 5 слов.', sep='\n')
s = '''Правила игры:
    - У тебя есть 6 попыток отгадать слово, состоящее из 5 букв.
    - Подсвечивающиеся буквы желтым цветом - значит ты угадал букву, но она не на своем месте.
    - Зеленая буква - значит ты угадал и букву, и место.
    - По истечению 6 попыток ты проигрываешь( Но можешь начать сначала!
'''
print(s)

# убираю из файла слова короче/длиннее 5
with open('word.txt', 'r+', encoding='utf-8') as file:
    word = []
    for i in file:
        if len(i) == 6:
            word.append(i.upper().strip())


# выбираю рандомное слово
secret = random.choice(word)
alphabet = 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ы Ъ Э Ю Я'

def game():
    global alphabet
    attempt = 6
    new_word = ''
    #запуская раунды
    while attempt != 0:
        print(secret)
        print('-'*10)
        print(f'Осталось {attempt} попыток.')
        print('-' * 10)
        s = input('Введите 5 букв: ').upper()
        print('-' * 10)
        print('-' * 10)

        #проверяю схожесть букв
        for i in range(5):

            if len(s) > 5:
                print('Вы ввели больше 5 букв')
                break
            elif len(s) < 5:
                print('Вы ввели меньше 5 букв')
                break

            letter = '' #буква для смены в алфавите
            if s[i] == secret[i]: #если индексы загаданного слова совпадает с веденным, то окрашиваю в зеленый
                new_word += Fore.GREEN + s[i] + Fore.RESET

                letter = Fore.GREEN + s[i] + Fore.RESET
                alphabet = alphabet.replace(s[i], letter)
            elif s[i] in secret: #если введенная буква есть в загаданном слове, то окрашиваю в желтый
                new_word += Fore.YELLOW + s[i] + Fore.RESET

                letter = Fore.YELLOW + s[i] + Fore.RESET
                alphabet = alphabet.replace(s[i], letter)
            else:
                new_word += s[i] #в противном случае просто добавляю в список
                alphabet = alphabet.replace(s[i], '-')

            #разбираемся с алфавитом

        print(new_word)
        print(alphabet)
        new_word = ''

        if s == secret:
            print(f'Вы отгадали слово {secret} с {attempt} попытки.\nПоздравляю!')
            break
            print('-' * 10)
        attempt -= 1

    if attempt == 0:
        print(f'Попытки кончились. Вы проиграли. Загаданное слово - {secret}')
        print('-' * 10)

while True:
    x = input('Нажмите enter, если хотите сыграть еще раз.\nЕсли хотите завершить игру нажмите любую букву')
    if x == '':
        game()
    else:
        print('Вы вышли из игры')
        break
