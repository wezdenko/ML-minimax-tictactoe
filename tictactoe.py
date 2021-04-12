
class TicTacToe:

    def __init__(self, grid=None):
        if grid is None:
            self.grid = Grid()
        else:
            self.grid = grid
        self.result = None

    def get_square(self, x, y):
        return self.grid.get_square(x, y)

    def get_empty_squares(self):
        empty_squares = []
        for square in self.grid:
            if square.is_empty():
                empty_squares.append(square)
        return empty_squares

    def set_mark(self, x, y, mark):
        return self.grid.set_mark(x, y, mark)

    def is_finished(self):
        # check columns
        for x in range(3):
            if not self.get_square(x, 0).is_empty():
                if (self.get_square(x, 0).mark == self.get_square(x, 1).mark and 
                    self.get_square(x, 1).mark == self.get_square(x, 2).mark):
                    self.result = self.get_square(x, 0).mark
                    return True

        # check rows:
        for y in range(3):
            if not self.get_square(0, y).is_empty():
                if (self.get_square(0, y).mark == self.get_square(1, y).mark and 
                    self.get_square(1, y).mark == self.get_square(2, y).mark):
                    self.result = self.get_square(0, y).mark
                    return True

        # check diagonals:
        if not self.get_square(1, 1).is_empty():
            if (self.get_square(0, 0).mark == self.get_square(1, 1).mark and 
                self.get_square(1, 1).mark == self.get_square(2, 2).mark):
                self.result = self.get_square(1, 1).mark
                return True

            if (self.get_square(2, 0).mark == self.get_square(1, 1).mark and 
                self.get_square(1, 1).mark == self.get_square(0, 2).mark):
                self.result = self.get_square(1, 1).mark
                return True

        # check if there's draw:
        if len(self.get_empty_squares()) == 0:
            self.result = 'Draw'
            return True
        return False

    def __repr__(self):
        grid_repr = ''
        for square in self.grid:
            if square.x == 2:
                grid_repr += f'{square}\n'
            else:
                grid_repr += f'{square}|'
        return grid_repr


class Grid(list):

    def __init__(self):
        grid = []
        for y in range(3):
            for x in range(3):
                grid.append(Square(x, y))
        super().__init__(grid)

    def get_square(self, x, y):
        return self[3*y + x]

    def set_mark(self, x, y, mark):
        self.get_square(x, y).mark = mark

    def copy(self):
        grid_copy = Grid()
        for i, square in enumerate(self):
            grid_copy[i].mark = square.mark
        return grid_copy

    def is_empty(self):
        for square in self:
            if not square.is_empty():
                return False
        return True

    def __eq__(self, other):
        for i in range(9):
            if self[i] != other[i]:
                return False
        return True



class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mark = None

    def is_empty(self):
        return True if self.mark is None else False

    def is_corner(self):
        if (self.x, self.y) in [(0, 0), (2, 0), (0, 2), (2, 2)]:
            return True
        return False

    def is_edge(self):
        if (self.x, self.y) in [(1, 0), (0, 1), (2, 1), (1, 2)]:
            return True
        return False

    def is_middle(self):
        return True if self.x == 1 and self.y == 1 else False

    def __repr__(self):
        return f'{self.mark}' if self.mark is not None else ' '

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                if self.mark == other.mark:
                    return True
        return False

