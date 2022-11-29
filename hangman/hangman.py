import random

while True:
    main_menu = input('''      Welcome to the HANGMAN !!!
  X_X Are you want start the game? :D
Please, enter (yes or somthing another
User: ''')
    if main_menu == "yes":
        words_list = ["python", "php", "java", "javascript"]
        random_word = random.choice(words_list)
        letter_of_word = list(random_word)
        close_word = list("-" * len(letter_of_word))
        tries = 8
        set_of_used_letters = set()

        while True:
            print(' '.join(close_word))
            print(f"Your try:{tries}")
            letter_of_user = input("Input a letter:")
            if len(letter_of_user) > 1:
                print("You should input a single letter.")
                continue
            if letter_of_user.isupper():
                print("Please enter a lowercase English letter.")
                continue
            for repeating_letter in set_of_used_letters:
                if letter_of_user == repeating_letter:
                    print("You've already guessed this letter.")
                    continue
            set_of_used_letters.update(letter_of_user)

            for iteration in letter_of_word:
                if iteration == letter_of_user:
                    close_word[(letter_of_word.index(iteration))] = letter_of_user
                    for counter_for_same_index in range(len(letter_of_word)):
                        if letter_of_word[(letter_of_word.index(iteration))] == letter_of_word[counter_for_same_index]:
                            close_word[counter_for_same_index] = letter_of_user
            if letter_of_user not in close_word:
                tries -= 1
                if tries == 0:
                    print("You lose")
                    break
            if close_word == letter_of_word:
                print("You survive!")
                break
    else:
        exit()
        break
        
