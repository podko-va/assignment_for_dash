import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = random.choice(word_list).upper()
        self.guessed_letters = []
        self.attempts_left = 6