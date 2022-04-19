import random


class MinesweeperBoard:

    def __init__(self, size):
        self.board = [['  .  ' if random.randrange(0, 10) < 8 else '  b  ' for _ in range(size)] for _ in range(size)]
        self.board_size = size

    def print_board(self, game_state):
        top = [" |" + str(i) + "| " for i in range(0, self.board_size)]
        print("     ", *top)
        if game_state == "playing":
            print_board = [['  .  ' if item == '  b  ' else item for item in line] for line in self.board]
        else:
            print_board = self.board
        for i in zip(top, *print_board):
            print("\n")
            print(*i)


class Minesweeper:
    def __init__(self, size):
        self.m_board = MinesweeperBoard(size)
        self.size = size
        self.state = "playing"

    def play(self):
        while self.state == "playing":
            self.m_board.print_board("playing")
            coords = [int(x) for x in (input("enter your move X, Y: ").split(','))]
            # print(coords)
            print("game still going ... " + str(self.game_won()))
            self.calculate_flags(coords[1], coords[0])

    def calculate_flags(self, i, j):
        if self.m_board.board[i][j] != '  b  ':
            self.check_flags_rec(i, j)
        else:
            print("boom")
            self.state = "lost"
        self.m_board.print_board(self.state)

    def game_won(self):
        won = False
        for i in self.m_board.board:
            for j in i:
                print(j)
                if j == '  .  ':
                    won = False
        return won

    # need to mark flags on cells found from check neighbors

    def check_flags_rec(self, row, col):
        if self.m_board.board[row][col] != '  b  ':
            flags = 0
            for x in range(max(0, row - 1), min(self.size, row + 2)):
                for y in range(max(0, col - 1), min(self.size, col + 2)):
                    if self.m_board.board[x][y] == '  b  ':
                        flags += 1
                        print(x, y)
                        print(str(flags))
            if flags == 0:
                self.m_board.board[row][col] = '     '
                self.check_neighbors_rec(row, col)
            else:
                self.m_board.board[row][col] = '  ' + str(flags) + '  '

    def check_neighbors_rec(self, row, col):
        for x in range(max(0, row - 1), min(self.size, row + 2)):
            for y in range(max(0, col - 1), min(self.size, col + 2)):
                if self.m_board.board[x][y] != '     ':
                    self.check_flags_rec(x, y)
                    if self.m_board.board[x][y] == '     ':
                        self.check_neighbors_rec(x, y)

    #
    # Replaced this iterative code below with the recursive versions above
    #
    #
    # def check_flags(self, row, col):
    #     flags = 0
    #     if col + 1 < self.size:
    #         if self.m_board.board[row][col + 1] == '  b  ':
    #             flags += 1
    #     if col - 1 >= 0:
    #         if self.m_board.board[row][col - 1] == '  b  ':
    #             flags += 1  # left
    #     if row + 1 < self.size:
    #         if self.m_board.board[row + 1][col] == '  b  ':
    #             flags += 1  # up
    #     if row - 1 >= 0:
    #         if self.m_board.board[row - 1][col] == '  b  ':
    #             flags += 1  # down
    #     if row + 1 < self.size and col + 1 < self.size:
    #         if self.m_board.board[row + 1][col + 1] == '  b  ':
    #             flags += 1  # upper-right
    #     if row + 1 < self.size and col - 1 >= 0:
    #         if self.m_board.board[row + 1][col - 1] == '  b  ':
    #             flags += 1  # upper-left
    #     if row - 1 >= 0 and col + 1 < self.size:
    #         if self.m_board.board[row - 1][col + 1] == '  b  ':
    #             flags += 1  # lower-right
    #     if row - 1 >= 0 and col - 1 >= 0:
    #         if self.m_board.board[row - 1][col - 1] == '  b  ':
    #             flags += 1  # lower-left
    #     return flags

    # def check_neighbors(self, row, col):
    #     print("check neighbors")
    #     if col + 1 < self.size:
    #         if self.m_board.board[row][col + 1] != '     ':
    #             f = self.check_flags(row, col + 1)
    #             print("f: " + str(f))
    #             if f == 0:
    #                 self.m_board.board[row][col + 1] = '     '
    #                 print("going right")
    #                 self.check_neighbors(row, col + 1)  # right
    #             else:
    #                 self.m_board.board[row][col + 1] = '  ' + str(f) + '  '
    #
    #     if col - 1 >= 0:
    #         if self.m_board.board[row][col - 1] != '     ':
    #             f = self.check_flags(row, col - 1)
    #             if f == 0:
    #                 self.m_board.board[row][col - 1] = '     '
    #                 print("going left")
    #                 self.check_neighbors(row, col - 1)  # left
    #             else:
    #                 self.m_board.board[row][col - 1] = '  ' + str(f) + '  '
    #     if row + 1 < self.size:
    #         if self.m_board.board[row + 1][col] != '     ':
    #             f = self.check_flags(row + 1, col)
    #             if f == 0:
    #                 self.m_board.board[row + 1][col] = '     '
    #                 print("going up")
    #                 self.check_neighbors(row + 1, col)  # up
    #             else:
    #                 self.m_board.board[row + 1][col] = '  ' + str(f) + '  '
    #     if row - 1 >= 0:
    #         if self.m_board.board[row - 1][col] != '     ':
    #             f = self.check_flags(row - 1, col)
    #             if f == 0:
    #                 self.m_board.board[row - 1][col] = '     '
    #                 print("going down")
    #                 self.check_neighbors(row - 1, col)  # down
    #             else:
    #                 self.m_board.board[row - 1][col] = '  ' + str(f) + '  '
    #     if row + 1 < self.size and col + 1 < self.size:
    #         if self.m_board.board[row + 1][col + 1] != '     ':
    #             f = self.check_flags(row + 1, col + 1)
    #             if f == 0:
    #                 self.m_board.board[row + 1][col + 1] = '     '
    #                 print("going up right")
    #                 self.check_neighbors(row + 1, col + 1)  # upper-right
    #             else:
    #                 self.m_board.board[row + 1][col + 1] = '  ' + str(f) + '  '
    #     if row + 1 < self.size and col - 1 >= 0:
    #         if self.m_board.board[row + 1][col - 1] != '     ':
    #             f = self.check_flags(row + 1, col - 1)
    #             if f == 0:
    #                 self.m_board.board[row + 1][col - 1] = '     '
    #                 print("going up left")
    #                 self.check_neighbors(row + 1, col - 1)  # upper-left
    #             else:
    #                 self.m_board.board[row + 1][col - 1] = '  ' + str(f) + '  '
    #     if row - 1 >= 0 and col + 1 < self.size:
    #         if self.m_board.board[row - 1][col + 1] != '     ':
    #             f = self.check_flags(row - 1, col + 1)
    #             if f == 0:
    #                 self.m_board.board[row - 1][col + 1] = '     '
    #                 print("going lower right")
    #                 self.check_neighbors(row - 1, col + 1)  # lower-right
    #             else:
    #                 self.m_board.board[row - 1][col + 1] = '  ' + str(f) + '  '
    #     if row - 1 >= 0 and col - 1 >= 0:
    #         if self.m_board.board[row - 1][col - 1] != '     ':
    #             f = self.check_flags(row - 1, col - 1)
    #
    #             if f == 0:
    #                 self.m_board.board[row - 1][col - 1] = '     '
    #                 print("going lower left")
    #                 self.check_neighbors(row - 1, col - 1)  # lower-left
    #             else:
    #                 self.m_board.board[row - 1][col - 1] = '  ' + str(f) + '  '
