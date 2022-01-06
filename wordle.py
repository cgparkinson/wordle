from termcolor import colored
import random
from time import sleep

with open('vocab.txt', 'r') as f:
    vocab = f.readlines()
    vocab = [line.replace('\n','') for line in vocab]
    vocab = [line for line in vocab if len(line) == 5]
with open('dictionary.txt', 'r') as f:
    dictionary = f.readlines()
    dictionary = [line.replace('\n','') for line in dictionary]
    dictionary = [line for line in dictionary if len(line) == 5]

finished = 0
correct_word = random.choice(vocab)
guesses = []
# print("DEBUG correct word is", correct_word)

def remove_first(word, letter):
    for character_ref in range(len(word)):
        character=word[character_ref]
        if letter==character:
            word[character_ref] = '?'
            return word
    raise(NotImplementedError)

while finished == 0:
    word_raw = input()
    colors = [None, None, None, None, None]
    print("\033[A                             \033[A")    # ansi escape arrow up then overwrite the line
    
    if word_raw not in dictionary:
        print(colored("invalid",'red'))
    else:
        guesses.append(word_raw)
        word = list(word_raw)
        filtered_correct_word = list(correct_word)
        for letter_ref in range(len(word)):
            if word[letter_ref]==correct_word[letter_ref]:
                colors[letter_ref] = 'green'
                filtered_correct_word[letter_ref] = '?'

        for letter_ref in range(len(word)):
            letter = word[letter_ref]

            if letter in filtered_correct_word:
                if not colors[letter_ref]:
                    colors[letter_ref] = 'yellow'
                filtered_correct_word = remove_first(filtered_correct_word, letter)

        for letter_ref in range(len(word)):
            print(colored(word[letter_ref], colors[letter_ref]), end='')
        print('')
    if word_raw == correct_word:
        finished=1
    if len(guesses) == 6:
        finished=1
        print("you suck. correct word was", correct_word)
