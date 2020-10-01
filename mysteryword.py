import random
def play_game():
    file_object = open(r'C:\Users\marl0\04coder\python\python-mystery-word-mjhow4\words.txt', 'r')
    words_list = file_object.readlines()
    random_word = random.choice(words_list)
    #print(random_word)
    #print("random word from list is:", random.choice(words_list))
    greeting = str(input("Welcome to Mystery Game! Choose Your Level of Difficulty. Easy: words with 4-6 characters; Normal: words with 6-8 characters; & Hard: words with 8 or more characters.  Please type Easy, Normal, or Hard: ").upper())
    if greeting == "EASY":
        easy_list = [word for word in words_list if len(word) >= 4 and len(word) <= 6]
        random_word = random.choice(easy_list)
        #print(random_word)
    elif greeting == "NORMAL":
        normal_list = [word for word in words_list if len(word) >= 6 and len(word) <= 8]
        random_word = random.choice(normal_list)
        #print(random_word)
    elif greeting == "HARD":
        hard_list = [word for word in words_list if len(word) >= 8]
        random_word = random.choice(hard_list)
        #print(random_word)
    else:
        print("Please type Easy, Normal, or Hard.")

    print("The Mystery Word contains", len(random_word), "letters.")
    guesses_remaining = 8
    used_letters = []
    building_word = []
    building_word_string = ''
    print("You have", guesses_remaining, "guesses remaining!")
    #comment this print line later
    #print(random_word)

    while guesses_remaining > -1:
        user_guess = str(input("Please select one letter: ").lower())
        if user_guess in random_word.lower():
            print(user_guess)
            original_len = len(random_word)
            print("_ "*original_len)
            print(random_word.index(user_guess))
            x = random_word.index(user_guess)
            if user_guess in building_word_string:
                None
            else:
                building_word.insert(x, user_guess)
            print(building_word)
            building_word_string = '' .join(building_word)
            print(building_word_string)
            #print(random_word.lower())
            if int(len(building_word_string)) + 1 == int(len(random_word)):
                print("You Won!")
                print("The Mystery Word was:", random_word)
                ask_user_play = str(input("Would you like to play, again? (Please enter Yes or No): ").upper())
                if ask_user_play == "YES":
                    play_game()
                else:
                    print("See ya next time!")
                    return
            else:
                None 
       
        else:
            if user_guess in used_letters:
                print("You have already used this letter. Try again!")
                guesses_remaining += 1
            else:
                None
            print("Incorrect choice, please try again!")
            guesses_remaining -= 1
            if guesses_remaining > 1:
                print("You have", guesses_remaining, "guesses remaining!")
            else:
                print("You have", guesses_remaining, "guess remaining!")
            used_letters.append(user_guess)
            print(used_letters)
            if guesses_remaining == 0:
                print("You Lose!")
                print("The Mystery Word was:", random_word)
                ask_user_play = str(input("Would you like to play, again? (Please enter Yes or No): ").upper())
                if ask_user_play == "YES":
                    play_game()
                else:
                    print("See ya next time!")
                    return
            else:
                None


play_game()
#game still has some issues to work out
#for one game does not work for duplicate letters in Mystery Word