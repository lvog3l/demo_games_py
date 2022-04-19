import random


class MastermindBoard:
    def __init__(self):
        self.empty_row = "| X | X | X | X | X ||  C  C/P ||"
        self.divider = "_________________________________"

    def print_turn(self, history, evaluation, playing, code):
        # print("\n")
        if playing:
            print(self.empty_row)
            print(self.divider)
            for entry, h_entry in zip(history, evaluation):
                print("| " + " | ".join(entry) + " ||  " + str(h_entry[0]) + "   " + str(h_entry[1]) + "  ||")
        else:
            print("The correct code was: ")
            print("| " + " | ".join(code))


def generate_code():
    code_bank = ["B", "W", "Y", "R", "G"]
    code = [code_bank[random.randint(0, 4)] for _ in range(5)]
    return code


class Mastermind:
    valid_chars = ["B", "W", "Y", "R", "G"]
    max_guesses = 8
    playing = 1
    won = 2
    lost = 3

    @staticmethod
    def input_is_valid(input_string):
        matches = [c in Mastermind.valid_chars for c in input_string]
        return len(matches) == 5 and all(matches)

    def __init__(self):
        self.board = MastermindBoard()
        self.history = []
        self.evaluation_history = []
        self.secret_code = generate_code()
        self.guesses = 0
        self.playing = True
        self.won = False

    def add_history(self, current_guess):
        self.history.insert(0, current_guess)

    def add_evaluation_history(self, current_history):
        self.evaluation_history.insert(0, current_history)

    def game_won(self, guess):
        matches = [i == j for i, j in zip(guess, self.secret_code)]
        return all(matches)

    def evaluate_guess(self, guess):
        temp = self.secret_code.copy()
        evaluation = [0, 0]
        for i in guess:
            if i in temp:
                evaluation[0] += 1
                temp[temp.index(i)] = '.'
        for i, j in zip(guess, self.secret_code):
            if i == j:
                evaluation[1] += 1
        return evaluation

    def play(self):
        print("Master Mind - a 5 part secret code has been generated out of black(B), yellow(Y), green(G), red(R), "
              "white(W)\n "
              "enter 5 letters (B, W, Y, R, G) separated by commas. if you aren't correct you will C P - how many of "
              "the correct color\n "
              "and how many of the correct color in the correct position")

        while self.playing:
            guess = input("Enter your guess: ").upper().split(",")
            if self.guesses >= 7:
                self.playing = False
                self.won = False
                print("Sorry you have no more guesses remaining.")
                self.board.print_turn(self.history, self.evaluation_history, self.playing, self.secret_code)
                return
            if Mastermind.input_is_valid(guess):
                self.guesses += 1
                evaluation = self.evaluate_guess(guess)
                self.add_history(guess)
                self.add_evaluation_history(evaluation)
                if self.game_won(guess):
                    self.won = True
                    self.playing = False
                    print("\nCongratulations! You guessed the secret code")
                else:
                    print("\nYou have " + str(8 - self.guesses) + " guesses remaining.\n")
                self.board.print_turn(self.history, self.evaluation_history, self.playing, self.secret_code)
            else:
                print("\nPlease enter 5 letters (B, W, Y, R, G) separated by commas")
