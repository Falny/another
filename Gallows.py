from colorama import init, Fore
from random import choice

init(convert=True)
HANG = ('''
    ------
     |    |
     |
     |
     |
     |
     |
    ----------
    ''',
        '''
        ------
         |    |
         |    0
         |
         |
         |
         |
        ----------
        ''',
        '''
        ------
         |    |
         |    0
         |    |
         |
         |
         |
        ----------
        ''',
        '''
        ------
         |    |
         |    0
         |   /|
         |
         |
         |
        ----------
        ''',
        '''
        ------
         |    |
         |    0
         |   /|\\
         |
         |
         |
        ----------
        ''',
        '''
        ------
         |    |
         |    0
         |   /|\\
         |   /
         |
         |
        ----------
        ''',
        '''
        ------
         |    |
         |    0
         |   /|\\
         |   / \\
         |
         |
        ----------
        '''
        )

alphabet = 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ы Ъ Э Ю Я'
FILENAME = 'word.txt'

def HangMan():
    global alphabet
    global HANG
    with open(FILENAME, 'r', encoding='utf-8') as f:
        file = [i.upper().strip() for i in f if len(i) == 5 and len(set(i)) == len(i)]

    flag = True
    count = 1
    secret = choice(file)
    main = ['_', '_', '_', '_']
    past_word = []
    print(secret)
    while flag:
        for i in range(2):
            print(HANG[count])
            if count == 6:
                flag = False
                print(f'Вы проиграли. Загаданное слово {secret}')
                break
            print()
            word = input('Введите букву: ').upper()
            if word in past_word: #проверяю на повтор букв
                print('Вы уже вводили эту букву')
                word = input('Введите новую букву: ').upper()
            past_word.append(word) #список для дуюлткатов букв
            if word in secret:
                index = secret.find(word)
                main[index] = word
                letter = Fore.GREEN + word + Fore.RESET
                alphabet = alphabet.replace(word, letter)
            else:
                alphabet = alphabet.replace(word, '-')
                count += 1

            print(*main)
            print()
            print(alphabet)

            if '_' not in main:
                print(f'Вы выйграли. Загаданное слово {secret}')
                flag = False


while True:
    x = input('Нажмите enter, если хотите сыграть еще раз.\nЕсли хотите завершить игру нажмите любую букву: ')
    if x == '':
        HangMan()
    else:
        print('Вы вышли из игры')
        break





