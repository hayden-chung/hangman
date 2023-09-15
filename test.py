import random

random_words = ['version', 'congress', 'pop', 'scan', 'swipe', 'mention', 'beam', 'portion', 'enjoy', 'kick']

random_word = random.choice(random_words)
status = ''
print('random', random_word)
for i in range(len(random_word)):
    status += '_'
print(status)
for i in range(self.attempts):
    print(f'remaining attempts: {self.attempts-i}')
    letter = input('Enter a letter:')
    if letter in random_word:
        for i in range(len(random_word)):
            if letter == random_word[i]:
                status_list = list(status)
                status_list[i] = letter
                status = ''.join(status_list)
        print(status)
    if status == random_word:
        print("YOU WIN")
        break