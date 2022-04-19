# import random
# from os import system
#
#
# def clear():
#     _ = system('clear')
#
#
# class HangmanBoard:
#     def __init__(self):
#         self.gallows = [["   __", "  |  |", "  |", "  |", "  |", "  |", "  |", "__|__"],
#                         ["   __", "  |  |", "  |  O", "  |", "  |", "  |", "  |", "__|__"],
#                         ["   __", "  |  |", "  |  O", "  |  |", "  |  |", "  |", "  |", "__|__"],
#                         ["   __", "  |  |", "  |  O", "  |  |", "  |  |", "  | /", "  |", "__|__"],
#                         ["   __", "  |  |", "  |  O", "  |  |", "  |  |", "  | / \\", "  |", "__|__"],
#                         ["   __", "  |  |", "  |  O", "  |  |/", "  |  |", "  | / \\", "  |", "__|__"],
#                         ["   __", "  |  |", "  |  O", "  | \\|/", "  |  |", "  | / \\", "  |", "__|__"]]
#
#     def print_turn(self, turn):
#         board_state = self.gallows[turn]
#         for i in board_state:
#             print(i)
#
#
# class MastermindBoard:
#     def __init__(self):
#         self.empty_row = "| X | X | X | X | X ||  C  C/P ||"
#         self.divider = "_________________________________"
#
#     def print_turn(self, history, evaluation, playing, code):
#         # print("\n")
#         if playing:
#             print(self.empty_row)
#         else:
#             print("| " + " | ".join(code) + " ||  C  C/P ||")
#         print(self.divider)
#         for entry, h_entry in zip(history, evaluation):
#             print("| " + " | ".join(entry) + " ||  " + str(h_entry[0]) + "   " + str(h_entry[1]) + "  ||")
#
#
# class IslandSurface:
#     def __init__(self, size, density):
#         self.size = size
#         self.density = density
#         self.surface = [['.' for i in range(size)] for j in range(size)]
#         self.print_surface()
#         for i in range(size):
#             for j in range(size):
#                 val = random.randrange(0, 100)
#                 if val < self.density:
#                     self.surface[i][j] = 'X'
#         self.print_surface()
#
#     def print_surface(self):
#         header = ['_ ' * self.size]
#         print(*header)
#         for row in self.surface:
#             print(*row)
#         print(*header)
#
#
# class MinesweeperBoard:
#
#     def __init__(self, size):
#         self.board = [['  .  ' if random.randrange(0, 10) < 8 else '  b  ' for _ in range(size)] for _ in range(size)]
#         self.board_size = size
#
#     def print_board(self, game_state):
#         top = [" |" + str(i) + "| " for i in range(0, self.board_size)]
#         print("     ", *top)
#         if game_state == "playing":
#             print_board = [['  .  ' if item == '  b  ' else item for item in line] for line in self.board]
#         else:
#             print_board = self.board
#         for i in zip(top, *print_board):
#             print("\n")
#             print(*i)
