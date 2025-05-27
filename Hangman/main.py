import random

guessed_letters = []
right_letters = []

def start_game_round():
    #find word
    word=find_word_from_file()
    #draw places
    print_game_place(0)
    print_word_place(word)
    #print(word)
    #init game loop
    start_game_loop(word)
        
def find_word_from_file():
    with open('./words.txt', 'r', encoding='UTF-8') as words:
        words_list = words.readlines()
    return random.choice(words_list).strip().lower()

def print_game_place(state):
    game_place = {
        0:   '''
                
                
                
                 
                
                
                ''',
        1:   ''' 
                
                
                
                
                 
                --- 
                ''',
        2:   '''
                | 
                | 
                | 
                |  
                |
                ---
                ''',
        3:   '''                 ----
                |
                | 
                | 
                |   
                |
                ---
                ''',
        4:   '''                 ----
                |  |
                | 
                | 
                |  
                |
                ---
                ''',
        5:   '''                 ----
                |  |
                |  0
                |
                | 
                |
                ---
                ''',
        6:   '''                 ----
                |  |
                |  0
                | /
                | 
                |
                ---
                ''',
        7:   '''                 ----
                |  |
                |  0
                | /|
                |   
                |
                ---
                ''',
        8:   '''                 ----
                |  |
                |  0
                | /|\\
                | 
                |
                ---
                ''',
        9:   '''                 ----
                |  |
                |  0
                | /|\\
                | /
                |
                ---
                ''',
        10:   '''                 ----
                |  |
                |  0
                | /|\\
                | / \\
                |
                ---
                ''',
    }
    print(game_place[state])
    
def print_word_place(word):
    global guessed_letters
    global right_letters
    print(' '.join([letter if letter in right_letters else '_' for letter in word]))    
    if len(guessed_letters)>0:
        print('Названные буквы:')
        print(' '.join(guessed_letters))
        print('#######################')
        
def start_game_loop(word):
    number_wrong_letters = 0
    global guessed_letters
    global right_letters
    
    #while game not over
    while number_wrong_letters<10:
        if len(right_letters) == len(set(word)):
            print('Поздравляю! Вы угадали слово!\n'+word.upper())
            return True           
        letter = input('Введите букву:').lower()
        #validate letter 
        if letter=='' or len(letter)>1 or 1072>ord(letter) or ord(letter)>1103:
            print('Введите одну русскую букву:')
        elif letter in guessed_letters:
            print('Эта буква уже была названа')
        else:
            guessed_letters.append(letter)            
            if letter in word:
                right_letters.append(letter)
                print('Поздравляю! Вы угадали букву!')
            else:
                number_wrong_letters+=1
                print_game_place(number_wrong_letters)
                if number_wrong_letters==10:
                    print('Игра окончена:')
                    print('Было задано слово: '+word.upper())
                    return True
            print_word_place(word)            
    
def main():
    global guessed_letters
    global right_letters
    while True:
        guessed_letters = []
        right_letters = []
        user_answer = input('хотите начать игру?да(y) или нет(n)\n')
        if user_answer in ['н','нет','n']:
            print('До свиданья!')
            exit()
        else:
            next_step = start_game_round()
    
if __name__ == "__main__":
    main()