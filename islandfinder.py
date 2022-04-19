import random


class IslandSurface:
    def __init__(self, size, density):
        self.size = size
        self.density = density
        self.surface = [[' . ' for i in range(size)] for j in range(size)]
        self.print_surface()
        for i in range(size):
            for j in range(size):
                val = random.randrange(0, 100)
                if val < self.density:
                    self.surface[i][j] = ' X '
        self.print_surface()

    def print_surface(self):
        header = ['_ ' * self.size]
        print(*header)
        for row in self.surface:
            print(*row)
        print(*header)


class IslandFinder:
    def __init__(self):
        self.num_islands = 0
        self.size = 0
        self.density = 0
        self.board = None

    def find_islands(self):
        print("This is a little recursive exercise for finding adjacent cells and labeling them")
        size = input("Define the NxN size of board (N = 1-20): ")
        density = input("Set the density of islands (1-100)")
        self.board = IslandSurface(int(size), int(density))
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.surface[i][j] == ' X ':
                    self.num_islands += 1
                    self.check_neighbors(i,j)
        self.board.print_surface()

    def check_neighbors(self, row, col):
        if self.board.surface[row][col] == ' X ':
            self.board.surface[row][col] = ' ' + str(self.num_islands) + ' '
            if col + 1 < self.board.size:
                self.check_neighbors(row, col+1)  # right
            if col - 1 >= 0:
                self.check_neighbors(row, col-1)  # left
            if row + 1 < self.board.size:
                self.check_neighbors(row+1, col)  # up
            if row - 1 >= 0:
                self.check_neighbors(row-1, col)  # down
            if row + 1 < self.board.size and col + 1 < self.board.size:
                self.check_neighbors(row+1, col+1)  # upper-right
            if row + 1 < self.board.size and col - 1 >= 0:
                self.check_neighbors(row+1, col-1)  # upper-left
            if row - 1 >= 0 and col + 1 < self.board.size:
                self.check_neighbors(row-1, col+1)  # lower-right
            if row - 1 >= 0 and col - 1 >= 0:
                self.check_neighbors(row-1, col-1)  # lower-left



