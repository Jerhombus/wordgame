import random
# Intro instructions
def intro():
    print(':+'*50)
    print("""                               Welcome to Guess The Word""")
    print(':+'*50)
# Splitting the letters in a word
def split(word):
    return [char for char in word]

#replaces Word needed to all underscores
def make_list_underscore(w_list):
    new_list = w_list 
    for i in range(len(new_list)):
        new_list[i] = '_'
    return new_list

def show_current(word, guessed_list):
    new_display= {}
    for letter in word:
        if letter in guessed_list:
            new_display.append(letter)
        else:
            new_display.append("_")
    print (" ".join(new_display))    
    
#User input. Returns the under_score list with the correct letters guessed.
def guess(underscore_list,w_list):
    u_input = input("What letter would you like to guess?: ").lower
    for k in range(len(underscore_list)):
        for i in w_list:
            if u_input == i and underscore_list[k] != w_list[k]:
                underscore_list[k] = w_list[k]
            elif u_input != i:
                print(i)
                print(w_list)
                print(underscore_list[k])
                return False
            else:
                print("You already entered that letter. Try again.")
    return underscore_list[k]
            

def get_new_word(w_list):
# takes a random word in a list and word_guess is that random word.
    r_num = random.randrange(len(w_list))
    word_guess = w_list[r_num]
    word_guess_list = split(word_guess)
    return word_guess_list
    

# r_num = random.randrange(len(w_list)):
# word_guess = w_list[r_num]
# word_guess_list = split(word_guess)
# word_guess_underscored = word_guess_list
# return make_list_underscore(word_guess_underscored)


wordlist = ['cat', 'dog', 'apple', 'program', 'python', 'lawyer', 'anaconda', 'starter', 'water']

# guessed = []
# limbs_left = 0



# guess(word_guess_list)


# Underscore per letter
# display_word = ' '
# for letter in word_guess_list:
#     if letter in guessed:
#         display_word += letter + " "
#     else:
#         display_word += "_"

times_allowed = 7
done = False
gameOver = False
while not done:
       #Asking if the user wants to play again after the game is over
       #Giving the user an option to quit the game
    # user_input = input("Would you like to quit: 'q'")
    # if user_input== 'q':
    #     break
    # else:
    intro()
    gameOver = False
    new_word = get_new_word(wordlist)
    u_word = new_word
    underscored_word = make_list_underscore(u_word)
    print(underscored_word)
    print(new_word)
    while not gameOver:
        print(guess(underscored_word,new_word))

    
#game will stop either when times_allowed decrease to 0, or when done = True, when word is guessed right 
    # guess()
    # for letter in word:
    #     print(letter)
    # for letter not in word:
    #     print("_")
    #     times_allowed -= 1
    #     if times_allowed == 0:
    #         break
    #     else:
    #         print(f"Try again! You have {times_allowed} times left")

