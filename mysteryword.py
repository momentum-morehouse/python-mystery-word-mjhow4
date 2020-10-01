import random
def play_game():
    file_object = open(r'C:\Users\marl0\04coder\python\python-mystery-word-mjhow4\words.txt', 'r')
    words_list = file_object.readlines()
    random_word = random.choice(words_list)
    #print(random_word)
    #print("random word from list is:", random.choice(words_list))
    greeting = str(input("Welcome to Mystery Game! Choose Your Level of Difficulty. Easy: words with 4-6 characters; Normal: words with 6-8 characters; & Hard: words with 8 or more characters.  Please type Easy, Normal, or Hard: ").upper())
    if greeting == "EASY":
        easy_list = [word for word in words_list if len(word) <= 6 and len(word) >= 4]
        random_word = random.choice(easy_list)
        #print(random_word)
    elif greeting == "NORMAL":
        normal_list = [word for word in words_list if len(word) <= 8 and len(word) >= 6]
        random_word = random.choice(normal_list)
        #print(random_word)
    elif greeting == "HARD":
        hard_list = [word for word in words_list if len(word) >= 8]
        random_word = random.choice(hard_list)
        #print(random_word)
    else:
        print("Please type Easy, Normal, or Hard.")

    print("The Mystery Word contains", len(random_word), "letters.")

play_game()