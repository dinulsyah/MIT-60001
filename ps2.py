# Problem Set 2, hangman.py
# Name:
# Collaborators:
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
    1. Dari secret_word kita ambil karakter unik dari var tersebut
    2. Jika semua karakter pada secret_word ada dalam list letter_guessed maka return 
       True otherwise False. okeeeee
    '''
    secret_word = set(secret_word)
    length_set = len(secret_word)
    true_char = 0
    
    for letter in letters_guessed:
        for char in secret_word:
            if letter == char:
                true_char = true_char+1
    
    if true_char == length_set:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    1. Simpan lah index var secret_word yang karakternya ada pada letter_guessed
    2. Buat sebuah string baru dengan melakukan checking pada seluruh index yang ada
       pada secret_word e.g 'apple' check pada index 0 sampai index 4.
       jika index terdapat dalam index_list maka gabungkan string dengan karakter dari
       index secret_word tersebut otherwise gabungkan string dengan "_ ".      
    '''
    index_list = list()
    length_set = len(secret_word)
    the_string = ''
    for letter in letters_guessed:
        for i in range(0,length_set):
            if letter == secret_word[i]:
                index_list.append(i) 
                
    for i in range(0,length_set):
        if i in index_list:
            the_string = the_string + secret_word[i]
        else:
            the_string = the_string + '_ '
    
    return the_string
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    1. buat list karakter alphabet pada list alphabet
    2. hapus karakter pada list alphabet jika karakter tersebut terdapat pada letters_guessed
    '''
    alphabet = list()
    for letter in string.ascii_lowercase:
        alphabet.append(letter)
    for letter in letters_guessed:
        if letter in alphabet:
            alphabet.remove(letter)
    alphabet = ''.join(alphabet)
    return alphabet

    
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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    available_warning = 3
    print("You have",available_warning,"warnings left")
    available_guess = 6
    #size_guess = len(secret_word)
    vowels = ['a','e','i','o','u']
    letters_guessed = list()
    while available_guess >= 1:
        print ("-------------------------")
        print ("You have",available_guess,"guess left")
        print ("available letters:",get_available_letters(letters_guessed))
        letter = str(input("Please guess a letter:"))
        letter = letter.lower()
        if letter in string.ascii_lowercase:
            if letter in letters_guessed:
                available_warning = available_warning - 1
                if available_warning < 0:
                    print("Oops! you've already guessed that letter. You have no warning left")
                    available_guess = available_guess - 1
                else:
                    print("Oops! you've already guessed that letter. You now have",available_warning,"warnings:",get_guessed_word(secret_word,letters_guessed))
            else:
                letters_guessed.append(letter)
                string_guessed = get_guessed_word(secret_word,letters_guessed)
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print ("Good guess:",string_guessed)
                    break
                elif letter in string_guessed:
                    print ("Good guess:",string_guessed)
                else:
                    print ("Oops! That letter is not in my word:",string_guessed)
                    if letter in vowels:
                        available_guess = available_guess - 2
                    else:
                        available_guess = available_guess - 1
        else:
            available_warning = available_warning - 1
            if available_warning < 0:
                print("Oops! That is not a valid letter. You have no warning left")
                available_guess = available_guess - 1
            else:
                print("Oops! That is not a valid letter. You have",available_warning,"warning left:",get_guessed_word(secret_word,letters_guessed))
    if available_guess==0:
        print("Sorry,you ran out of guesses. The word was",secret_word)
    else:
        print("Congratulations, you won!")
        print("Your total score for this game is:",len(set(secret_word))*available_guess)
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
    my_word=my_word.replace(" ","")
    my_length = len(my_word)
    other_length = len(other_word)
    number = 0
    temp = 0
    alpha_list = list()
    word_list = list()
    for char in string.ascii_lowercase:
        alpha_list.append(char)
    for char in set(my_word):
        word_list.append(char)
    for char in word_list:
        if char in alpha_list:
            alpha_list.remove(char)
    for char in my_word:
        if char in string.ascii_lowercase:
            number=number+1
    if my_length == other_length:
        for i in range(0,my_length):
            if my_word[i] == other_word[i]:
                temp = temp + 1
                if temp == number:
                    return True
            else:
                if other_word[i] not in alpha_list:
                    return False
                if my_word[i] in string.ascii_lowercase:
                    if my_word[i] != other_word[i]:
                        return False
    else:
        return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    true_word = list()
    for word in wordlist:
        if match_with_gaps(my_word, word)==True:
            true_word.append(word)
    if len(true_word)==0:
        print("no matches found")
    return "   ".join(true_word)

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    available_warning = 3
    print("You have",available_warning,"warnings left")
    available_guess = 6
    #size_guess = len(secret_word)
    vowels = ['a','e','i','o','u']
    asterisk = "*"
    letters_guessed = list()
    while available_guess >= 1:
        print ("-------------------------")
        print ("You have",available_guess,"guess left")
        print ("available letters:",get_available_letters(letters_guessed))
        letter = str(input("Please guess a letter:"))
        letter = letter.lower()
        if letter in string.ascii_lowercase:
            if letter in letters_guessed:
                available_warning = available_warning - 1
                if available_warning < 0:
                    print("Oops! you've already guessed that letter. You have no warning left")
                    available_guess = available_guess - 1
                else:
                    print("Oops! you've already guessed that letter. You now have",available_warning,"warnings:",get_guessed_word(secret_word,letters_guessed))
            else:
                letters_guessed.append(letter)
                string_guessed = get_guessed_word(secret_word,letters_guessed)
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print ("Good guess:",string_guessed)
                    break
                elif letter in string_guessed:
                    print ("Good guess:",string_guessed)
                else:
                    print ("Oops! That letter is not in my word:",string_guessed)
                    if letter in vowels:
                        available_guess = available_guess - 2
                    else:
                        available_guess = available_guess - 1
        elif letter==asterisk:
            print(show_possible_matches(string_guessed))
        else:
            available_warning = available_warning - 1
            if available_warning < 0:
                print("Oops! That is not a valid letter. You have no warning left")
                available_guess = available_guess - 1
            else:
                print("Oops! That is not a valid letter. You have",available_warning,"warning left:",get_guessed_word(secret_word,letters_guessed))
    if available_guess==0:
        print("Sorry,you ran out of guesses. The word was",secret_word)
    else:
        print("Congratulations, you won!")
        print("Your total score for this game is:",len(set(secret_word))*available_guess)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #secret_word = choose_word(wordlist)
    #print(secret_word)
    hangman_with_hints(wordlist)
    

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
