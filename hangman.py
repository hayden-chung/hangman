import random

random_words = ['version', 'congress', 'pop', 'scan', 'swipe', 'mention', 'beam', 'portion', 'enjoy', 'kick']



class HangManGame ():
    def __init__(self, attempts):
        self.attempts = attempts
        self.my_string = ''
        self.random_word = None

    
    def get_random_words(self):
        pass

    def make_empty_string(self):
        self.random_word = random.choice(random_words)
        for i in range(len(self.random_word)):
            self.my_string += '_'
        

    def play(self):
        self.make_empty_string()
        print(self.my_string)
        print(self.random_word)
        for i in range(self.attempts):
            print(f'remaining attempts: {self.attempts-i}')
            letter = input('Enter a letter:')
            if letter in self.random_word:
                for i in range(len(self.random_word)):
                    if letter == self.random_word[i]:
                        my_string_list = list(self.my_string)
                        my_string_list[i] = letter
                        self.my_string = ''.join(my_string_list)
                print(self.my_string)
            if self.my_string == self.random_word:
                print("YOU WIN")
                break




game1 = HangManGame(7)
game1.play()
