from wordList import words
import random
import string

def get_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alpha = set(string.ascii_uppercase)
    used_letters = set()

    wrongSelect = 10

    while(wrongSelect>0 and len(word_letters)>0):
        print("\nNo. of Lives Left : ",wrongSelect)
        print('Already Chosen Alphabets : ',' '.join(used_letters))


        # current progress
        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current Word:: ',' '.join(word_list))

        user_letter = input("Guess the Alphabets ::").upper()

        if user_letter in alpha - used_letters:
            used_letters.add(user_letter)

            if(user_letter) in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                wrongSelect-=1
                print("Wrong Guess !")
        elif (user_letter in used_letters):
            print("Already Guessed")
        else:
            print("Invalid Key Entered !")
    
    if(wrongSelect==0):
        print("YOU LOST ! Word was ::",word)
    else:
        print("YOU WON ! Word is ::",word)


if __name__ == '__main__':
    hangman()