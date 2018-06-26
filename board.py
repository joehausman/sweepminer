import random

class position:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_pos(self):
        print('cell: ' + str(self.x) + ', ' + str(self.y))  # DEBUGGING

class board:
    height = 0
    width = 0
    mines = 0
    grid = []
    visibility = []

    def at_position(self, cell):
        return self.grid[cell.y][cell.x]

    def set_cell(self, cell, val):
        self.grid[cell.y][cell.x] = val

    def increment_cell(self, cell):
        if self.at_position(cell) != -1:
            self.grid[cell.y][cell.x] += 1

    def is_mine(self, cell):
        return self.at_position(cell) == -1

    def is_off_board(self, cell):
        return cell.x < 0 or cell.x >= self.width \
            or cell.y < 0 or cell.y >= self.height

    def cell_adj(self, cell):
        x = cell.x
        y = cell.y
        i = x-1
        while i <= x+1:
            j = y-1
            while j <= y+1:
                temp = position(i, j)
                if not self.is_off_board(temp) and self.is_mine(temp):
                    self.increment_cell(cell)
                j += 1
            i += 1

    def calculate_adj(self):
        # @TODO: consider more elegant solution
        #           update adjacencies for surrounding cells
        #               when placing a mine
        #           rather than iterating through the entire grid afterward
        for i in range(self.height):
            for j in range(self.width):
                cell = position(j, i)
                if not self.is_mine(cell):
                    self.cell_adj(cell)

    def random_position(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        return position(x, y)


    def create_grid(self):
        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append(0)

    def place_mines(self, num_mines):
        while num_mines > 0:
            curr_mine = self.random_position()
            if self.at_position(curr_mine) != -1:
                self.set_cell(curr_mine, -1)
                num_mines -= 1

    def create_visibility(self):
        for i in range(self.height):
            self.visibility.append([])
            for j in range(self.width):
                self.visibility[i].append(False)


    def print_board(self):
        for i in self.grid:
            print(str(i))

    def print_visibility(self):
        for row in visibility:
            print(''.join(row))


    def debugging_mines(self):
        self.grid[0] = [0, 0, -1, 0, 0]
        self.grid[1] = [0, -1, -1, 0, 0]
        self.grid[2] = [0, 0, 0, 0, 0]
        self.grid[3] = [0, 0, -1, 0, 0]
        self.grid[4] = [0, 0, 0, 0, -1]

    def __init__(self, num_height, num_width, num_mines):
        # @TODO: error out / throw exception if bad number of height / width
        self.height = num_height
        self.width = num_width
        self.mines = num_mines
        self.create_grid()
        self.place_mines(num_mines)
        self.calculate_adj()
        self.create_visibility()
