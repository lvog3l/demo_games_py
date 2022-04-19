import random


class HangmanBoard:
    def __init__(self):
        self.gallows = [["   __", "  |  |", "  |", "  |", "  |", "  |", "  |", "__|__"],
                        ["   __", "  |  |", "  |  O", "  |", "  |", "  |", "  |", "__|__"],
                        ["   __", "  |  |", "  |  O", "  |  |", "  |  |", "  |", "  |", "__|__"],
                        ["   __", "  |  |", "  |  O", "  |  |", "  |  |", "  | /", "  |", "__|__"],
                        ["   __", "  |  |", "  |  O", "  |  |", "  |  |", "  | / \\", "  |", "__|__"],
                        ["   __", "  |  |", "  |  O", "  |  |/", "  |  |", "  | / \\", "  |", "__|__"],
                        ["   __", "  |  |", "  |  O", "  | \\|/", "  |  |", "  | / \\", "  |", "__|__"]]

    def print_turn(self, turn):
        board_state = self.gallows[turn]
        for i in board_state:
            print(i)


class Hangman:
    win = 0
    lose = 1
    active = 2
    max_guesses = 6

    def __init__(self):
        self.board = HangmanBoard()
        self.game_states = ["win", "lose", "active"]
        self.num_incorrect_guesses = 0
        self.state = "active"
        self.puzzle_word = ''
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.word_list = []
        with open("words.txt", "r") as f:
            for _ in f:
                self.word_list = f.read().splitlines()

    def set_game_state(self, gs):
        self.state = self.game_states[gs]

    def get_game_state(self):
        return self.state

    def print_game_turn(self, turn):
        self.board.print_turn(turn)

    def generate_word(self, word_length):
        self.puzzle_word = ''
        while len(self.puzzle_word) != word_length or "\'" in self.puzzle_word:
            self.puzzle_word = self.word_list[random.randrange(0, len(self.word_list))]
        self.correct_guesses = ['_'] * len(self.puzzle_word)

    def guess(self, letter):
        if letter in self.puzzle_word:
            for i, c in enumerate(self.puzzle_word):
                if c == letter:
                    self.correct_guesses[i] = c
            return True
        else:
            self.incorrect_guesses.append(letter)
            # print(self.incorrect_guesses)
            return False

    def guess_exists(self, letter):
        if letter in self.incorrect_guesses or letter in self.correct_guesses:
            return True

    def get_correct_guesses(self):
        return self.correct_guesses

    def get_incorrect_guesses(self):
        return self.incorrect_guesses

    def play(self):
        word_length = input("Enter length of word you'd like to guess (5-12 chars): ")
        self.generate_word(int(word_length))
        self.board.print_turn(0)
        while self.get_game_state() == self.game_states[Hangman.active]:
            guess = input("Enter a letter: ")
            if self.guess_exists(guess):
                print("You've already tried " + guess)
            elif self.guess(guess):
                puzzle = "".join(self.puzzle_word)
                guesses = "".join(self.correct_guesses)
                if guesses == puzzle:
                    print("You Win! the word is: " + str(self.puzzle_word))
                    self.set_game_state(Hangman.win)
                else:
                    print("Correct!")
                    self.board.print_turn(self.num_incorrect_guesses)
                    print(*self.correct_guesses)
                    temp = ", ".join(self.incorrect_guesses)
                    print("Guesses " + temp)
            else:
                print("Incorrect")
                self.num_incorrect_guesses += 1
                self.board.print_turn(self.num_incorrect_guesses)
                print(*self.correct_guesses)
                temp = ", ".join(self.incorrect_guesses)
                print("Guesses " + temp)
                if self.num_incorrect_guesses == Hangman.max_guesses:
                    self.set_game_state(Hangman.lose)
                    print("Sorry you lose - the word is: " + self.puzzle_word)
