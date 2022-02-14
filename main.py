#!/bin/python3
import random
import time
import string

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open('vocab.txt', 'r') as f:
    vocab = f.readlines()
    vocab = [line.replace('\n','') for line in vocab]
    vocab = [line for line in vocab if len(line) == 5]
with open('dictionary.txt', 'r') as f:
    dictionary = f.readlines()
    dictionary = [line.replace('\n','') for line in dictionary]
    dictionary = [line for line in dictionary if len(line) == 5]

dictionary = dictionary + vocab
finished = 0
seed = int(time.time()/60)
random.seed(int(seed))
print("Welcome to Fake Wordle.\nA new word every minute.\nIf playing with a friend, \ncheck this number is the \nsame for all players: " + str(seed)[-2:])
print("=========================")
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

def print_letters(correct_word, guesses):
    letters = list(string.ascii_lowercase)
    guesses_concat = [letter for guess in guesses for letter in guess]
    print("=========================")
    for letter in letters:
        if letter in guesses_concat and letter not in correct_word:
            pass
        elif letter in guesses_concat:
            print(bcolors.WARNING + letter + bcolors.ENDC, end='')
        elif letter not in guesses_concat:
            print(letter, end='')
    print("")
    print("=========================")

while finished == 0:
    print_letters(correct_word, guesses)
    word_raw = input()
    colors = [None, None, None, None, None]
    print("\033[A                             \033[A")    # ansi escape arrow up then overwrite the line
    print("\033[A                                              \033[A")    # ansi escape arrow up then overwrite the line
    print("\033[A                                              \033[A")    # ansi escape arrow up then overwrite the line
    print("\033[A                                              \033[A")    # ansi escape arrow up then overwrite the line
    
    if word_raw not in dictionary:
        print(bcolors.FAIL + "invalid" + bcolors.ENDC)
    else:
        guesses.append(word_raw)
        word = list(word_raw)
        filtered_correct_word = list(correct_word)
        for letter_ref in range(len(word)):
            if word[letter_ref]==correct_word[letter_ref]:
                colors[letter_ref] = bcolors.OKGREEN
                filtered_correct_word[letter_ref] = '?'

        for letter_ref in range(len(word)):
            letter = word[letter_ref]

            if letter in filtered_correct_word:
                if not colors[letter_ref]:
                    colors[letter_ref] = bcolors.WARNING
                    filtered_correct_word = remove_first(filtered_correct_word, letter)

        for letter_ref in range(len(word)):
            color = colors[letter_ref] if colors[letter_ref] else ""
            print(color + word[letter_ref] + bcolors.ENDC, end='')
        print('')
    if word_raw == correct_word:
        finished=1
    elif len(guesses) == 6:
        finished=1
        print("you suck. correct word was", correct_word)
