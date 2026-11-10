def game():
    word = 'hammam'
    word_secure = ['_'] * len(word)
    enabled = True
    counter = 6

    while enabled:
        print('осталось', counter, 'попыток')
        print(' '.join(word_secure))
        if '_' not in word_secure:
            print('поздравляем, вы выиграли. Слово:', word)
            break
        letter = input('введите букву: ')
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_secure[i] = letter
        else:
            counter -= 1
            print('такой буквы нет')
        if counter == 0:
            print('вы проиграли, загаданное слово было:', word)
            enabled = False

game()
