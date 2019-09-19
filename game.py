import random


class alooGame:
    def __init__(self):
        self.score = 0

    print("******** Welcome To Alooo Game ********")

    # global score

    def name(self):
        # while True: //costly
        playerName = input("Enter your name : ")
        if not playerName.isalpha():
            exit(-1)

            # print("Please enter characters A-Z only")
        return playerName

    def easy(self):
        E = ["plane", "laptop", "pencil", "paper",
             "school", "gamer", "action", "healthy"]
        return random.choice(E)

    def medium(self):
        M = ["beautiful", "expensive", "professor", "exercise"]
        return random.choice(M)

    def hard(self):
        H = ["envirement", "photography", "university"]
        return random.choice(H)

    """def list_initialization():
        e = ["Plane","Laptop","Pencil", "Paper","School","Gamer","Action","Healthy"]
        m = ["Beautiful","Expensive", "Professor","Exercise"]
        h = ["Envirement","Photography", "University"]"""

    def display_menu(self):
        print("============================")
        print("     Choose difficulty")
        print("     E - Easy, word of 5+ letters")
        print("     M - Medium, word of 8+ letters")
        print("     H - Hard, word of 10+ letters")
        print("     Q - Quit")

    def generate_word_with_missing_letters(self, my_list, E):
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

    def player(self, word):
        print("Guess the word. You have only 3 tries!")
        print(word)
        t = 3
        test = False
        while (t > 0 or test == False):
            print("Please enter the correct word (You still have ", t, " tries):")
            while True:
                guess = input("word = ")
                if guess.isalpha():
                    break
                print("Please enter characters A-Z only")

            if guess == word:
                self.score += 1
                print("Congratulations ! You did it :)")
                t = t-1
                test = True
                break
            else:
                print("Incorrect word :(")
                if(t == 1):
                    print("You lost, the correct word is ", word)
                t = t-1

    def game(self, my_list):
        result = ""
        # score = 0
        while (result != "Q"):
            self.display_menu()
            result = input("Select your choice")

            if (result == "E"):
                E = self.easy()
                self.generate_word_with_missing_letters(my_list, E)
                self.player(E)
                # self.player(self.score, E)

            elif (result == "M"):
                M = self.medium()
                self.generate_word_with_missing_letters(my_list, M)
                self.player(M)
                # self.player(self.score, M)

            elif (result == "H"):
                H = self.hard()
                self.generate_word_with_missing_letters(my_list, H)
                self.player(H)
                # self.player(self.score, H)

            else:
                print("You didn't choose the correct choice ! Try again.")

        if(result == "Q"):
            print("Your score is ", self.score)


alooPlayer = alooGame()
alooPlayer.name()
alooPlayer.game([])
