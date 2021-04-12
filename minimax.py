from tictactoe import TicTacToe, Grid, Square


class State:

    def __init__(self, grid=Grid(), previous_state=None, is_max=True):
        self.grid = grid
        self.is_max = is_max
        self.previous_state = previous_state
        self.successors = []
        self.value = 0

    def is_terminal(self):
        game = TicTacToe(self.grid)
        return True if game.is_finished() else False


def minimax(state, depth):
    # zwrócenie wartości stanu w przypadku stanu terminalnego
    if state.is_terminal():
        state.value = payment(state) * 100
        return state

    # zwrócenie wartości stanu gdy osiągniemy maksymalną głębokość
    if depth == 0:
        state.value = evaluate_move(state)
        return state
    
    # wygenerowanie następnych stanów
    state.successors = successors(state)

    # obliczenie wypłaty dla kolejnych stanów
    for next_state in state.successors:
        next_state.value = minimax(next_state, depth - 1).value

    # zwrócenie najlepszego ruchu
    if state.is_max:
        state.value = max([successor.value for successor in state.successors])
        return state
    else:
        state.value = min([successor.value for successor in state.successors])
        return state


def payment(state):
    game = TicTacToe(state.grid)
    if game.is_finished():
        if game.result == 'O':
            return 1
        if game.result == 'X':
            return -1
    return 0


def evaluate_move(state):
    # 3|2|3
    # 2|4|2
    # 3|2|3
    #
    # win = 100

    score = 0

    def calculate_points(square, points):
        if square.mark == 'O':
            return points
        if square.mark == 'X':
            return -points
        return 0

    for square in state.grid:
        if square.is_edge():
            score += calculate_points(square, 2)
        if square.is_corner():
            score += calculate_points(square, 3)
        if square.is_middle():
            score += calculate_points(square, 4)
    return score


def successors(state):
    next_states = []

    # przy pierwszym stanie wybor 3 nastepnych zamiast 9 (dla optymalizacji)
    if state.grid.is_empty():
        for i in range(3):
            new_grid = Grid()
            new_grid[i**2].mark = 'O'
            next_states.append(State(new_grid, state, is_max=False))
        return next_states

    # wybor nastepnych stanow
    for square in state.grid:
        if square.is_empty():

            new_grid = state.grid.copy()

            if state.is_max:
                new_grid.get_square(square.x, square.y).mark = 'O'
                next_states.append(State(new_grid, state, is_max=False))
            else:
                new_grid.get_square(square.x, square.y).mark = 'X'
                next_states.append(State(new_grid, state, is_max=True))

    return next_states


class MinimaxPlayer:

    def __init__(self, game, mark, depth):
        self.mark = mark
        self.game = game
        self.depth = depth

    def is_max(self):
        if self.mark == 'O':
            return True
        return False

    def make_move(self):
        state = State(self.game.grid, is_max=self.is_max())
        current_state = minimax(state, self.depth)

        # wybor nastepnego ruchu
        next_move = None
        for successor in current_state.successors:
            if current_state.value == successor.value:
                self.game.grid = successor.grid.copy()
                self.states_tree = successor
                break

