import random

class position:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class board:
    height = 0
    width = 0
    mines = 0
    grid = []
    visibility = []

    def at_position(self, cell):
        return self.grid[cell.y][cell.x]

    def set_cell(self, cell, val):
        grid[cell.y][cell.x] = val

    def increment_cell(self, cell):
        if at_position(cell) != -1
            grid[cell.y][cell.x] += 1

    def is_mine(self, cell):
        return self.at_position(cell) == -1

    def is_off_board(self, cell):
        return cell.x < 0 or cell.x >= width \
            or cell.y < 0 or cell.y >= height

    def adj_list(self, cell):
        adj = []
        x = cell.x
        y = cell.y

        # top
        for i in range(x-1, x+1):
            adj.append(position(i, y-1))
        # middle
        adj.append(position(x-1, y))
        adj.append(position(x+1, y))
        # bottom
        for i in range(x-1, x+1):
            adj.append(position(i, y+1))

        # remove out-of-bounds cells
        for cell in adj:
            if is_off_board(cell):
                adj.remove(cell)

        return adj

    def random_position(self):
        x = randint(0, width-1)
        y = randint(0, height-1)
        return position(x, y)


    #-----

    def create_grid(self):
        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append(0)

    def place_mines(self, num_mines):
        while num_mines > 0:
            curr_mine = self.random_position()
            if at_position(curr_mine) != -1:
                set_cell(curr_mine, -1)
                update_adj(curr_mine)
                num_mines -= 1

    def update_adj(self, cell):
        adjacent = adj_list(cell)
        for x in adj_list:
            increment_cell(x)

    def create_visibility(self):
        for i in range(self.height):
            self.visibility.append([])
            for j in range(self.width):
                self.visibility[i].append(False)

    def __init__(self, num_height, num_width, num_mines):
        # @TODO: error out / throw exception if bad number of height / width

        self.height = num_height
        self.width = num_width
        self.mines = num_mines
        self.create_grid()
        self.place_mines(num_mines)
        self.create_visibility()
