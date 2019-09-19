import random


print("******** Welcome To Alooo Game ********")



def name():
    while True:
        name = input("Enter your name : ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only")
    return name

def easy():
    E = ["plane", "laptop", "pencil", "paper", "school", "gamer", "action", "healthy"]
    return random.choice(E)

def medium():
    M = ["beautiful","expensive", "professor","exercise"]
    return random.choice(M)

def hard():
    H  = ["envirement","photography", "university"]
    return random.choice(H)

"""def list_initialization():
    e = ["Plane","Laptop","Pencil", "Paper","School","Gamer","Action","Healthy"]
    m = ["Beautiful","Expensive", "Professor","Exercise"]
    h = ["Envirement","Photography", "University"]"""

def display_menu():
    print("============================")
    print("     Choose difficulty")
    print("     E - Easy, word of 5+ letters")
    print("     M - Medium, word of 8+ letters")
    print("     H - Hard, word of 10+ letters")
    print("     Q - Quit")

def generate_word_with_missing_letters(my_list,E):
    word = E

    i = int(len(word) / 2)
    test = False
    while (test == False):
        word_game = word
        j = 0
        while (j < i):
            r = random.randint(0, len(word) - 1)
            if (word_game[r] != "_"):
                word_game = word_game.replace(word_game[r], "_")
                j = j + 1

        if (word_game in my_list):
            test = False
            print("The elements of the list are", my_list)
        else:
            my_list.append(word_game)
            print(word_game)
            test = True


def player(score, word):
    print("Guess the word. You have only 3 tries!")
    t = 3
    test = False
    while (t >0 or test == False):
        print("Please enter the correct word (You still have ",t," tries):")
        while True:
            guess = input("word = ")
            if guess.isalpha():
                break
            print("Please enter characters A-Z only")

        if guess == word:
            score = score + 1
            print("Congratulations ! You did it :)")
            t = t-1
            test = True
            break
        else:
            print("Incorrect word :(")
            if(t == 1):
                print("You lost, the correct word is ",word)
            t = t-1







def game(self,my_list):
    result=""
    self.score = 0
    while (result != "Q"):
        display_menu()
        result = input("Select your choice")


        if (result == "E"):
            E = easy()
            generate_word_with_missing_letters(my_list,E)
            player(self.score, E)

        elif (result == "M"):
            M = medium()
            generate_word_with_missing_letters(my_list,M)
            player(self.score, M)

        elif (result == "H"):
            H = hard()
            generate_word_with_missing_letters(my_list,H)
            player(self.score, H)

        else:
            print("You didn't choose the correct choice ! Try again.")

    if(result == "Q"):
        print("Your score is ",score)
















