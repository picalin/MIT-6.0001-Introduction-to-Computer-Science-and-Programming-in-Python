# Problem Set 2, hangman.py
# Name: Hikaru Shoda
# Collaborators:None
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()




def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_guessed = []
    for letter in secret_word:
        word_guessed.append(letter in letters_guessed)
    return all(word_guessed)
# print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_guessed = []
    for letter in secret_word:
        if (letter in letters_guessed) == True:
            word_guessed.append(letter)
        else:
            word_guessed.append("_ ")
    return "".join(word_guessed)

# print(get_guessed_word(secret_word, letters_guessed))

#get available letters#

def get_available_letters(letters_guessed):
    '''b
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = []
    for letter in string.ascii_lowercase:
        if (letter in letters_guessed) == False:
            available_letters.append(letter)    
    return "".join(available_letters)

# print(get_available_letters(letters_guessed))
    
    
# Hangaman code below #
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #Welcome Message
    print("\nWelcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    print("You have 3 warnings remaining")
    print("\n----------------------\n")
    #set the counter number and letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    warning_letters_guessed = []
    vowels = 'aeiou' 
    #number_of_unique_word_in_secret_word 
    number_of_unique_word_in_secret_word = len(set(secret_word))
    
    #game loop
    while guesses_remaining > 0 and warnings_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("You have " + str(guesses_remaining) + " guesses remaining")
        print("Available letters: ", get_available_letters(letters_guessed))
        word1 = input("Please guess a letter: ")
        letters_guessed.append(word1)
        if word1 not in string.ascii_lowercase:
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have " + str(guesses_remaining) + " guesses left", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left", get_guessed_word(secret_word, letters_guessed))
        elif word1 in warning_letters_guessed:
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have " + str(guesses_remaining) + " guesses left", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have " + str(warnings_remaining) + " warnings left", get_guessed_word(secret_word, letters_guessed))
        elif word1 in secret_word: #Good Guess
            print("Good Guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if word1 in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        warning_letters_guessed.append(word1)
        print("\n----------------------\n")
        
    '''↓↓↓↓after game finished↓↓↓↓↓'''  
    if guesses_remaining == 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word)
    else:
        Totall_Score = guesses_remaining * number_of_unique_word_in_secret_word
        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(Totall_Score))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    same_place_word = []
    no_space_my_word = my_word.replace(" ","")
    if len(no_space_my_word) == len(other_word):
        for i in range(len(no_space_my_word)):
            if no_space_my_word[i] == other_word[i]:
                same_place_word.append(my_word[i])
    return get_guessed_word(other_word, my_word) == my_word

# print(match_with_gaps("a_ _ le", "apple"))
# print(match_with_gaps("a_ ple", "apple"))
            
            
            
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = str()
    
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            possible_matches += other_word + ' '
    if possible_matches == '':
        print('No matches found')
    else:
        return possible_matches
# print(show_possible_matches("t_ _ t"))
            
            
    


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("\nWelcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    print("You have 3 warnings remaining")
    print("You can see the word matches if you input '*'")
    print("\n----------------------\n")
    #set the counter number and letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    warning_letters_guessed = []
    vowels = 'aeiou'
    
    #number_of_unique_word_in_secret_word 
    number_of_unique_word_in_secret_word = len(set(secret_word))
    
    #game loop
    while guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("You have " + str(guesses_remaining) + " guesses remaining")
        print("Available letters: ", get_available_letters(letters_guessed))
        word1 = input("Please guess a letter: ")
        letters_guessed.append(word1)
        if word1 == "*":
            print("Possible word matches are:")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        elif word1 not in string.ascii_lowercase:
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have " + str(guesses_remaining) + " guesses left", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left", get_guessed_word(secret_word, letters_guessed))
        elif word1 in warning_letters_guessed:
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have " + str(guesses_remaining) + " guesses left", get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have " + str(warnings_remaining) + " warnings left", get_guessed_word(secret_word, letters_guessed))
        elif word1 in secret_word: #Good Guess
            print("Good Guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if word1 in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        warning_letters_guessed.append(word1)
        print("\n----------------------\n")
        
    '''↓↓↓↓after game finished↓↓↓↓↓'''  
    if guesses_remaining == 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word)
    else:
        Totall_Score = guesses_remaining * number_of_unique_word_in_secret_word
        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(Totall_Score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

