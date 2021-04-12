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


def minimax_full(state):
    # zwrócenie wartości stanu w przypadku stanu terminalnego
    if state.is_terminal():
        state.value = payment(state)
        return state
    
    # wygenerowanie następnych stanów
    state.successors = successors(state)

    # obliczenie wypłaty dla kolejnych stanów
    for next_state in state.successors:
        next_state.value = minimax_full(next_state).value

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


class FullPlayer:

    def __init__(self, game, mark, tree=None):
        self.mark = mark
        self.game = game
        if tree is None:
            initial_state = State()
            self.states_tree = minimax_full(initial_state)
        else:
            self.states_tree = tree

    def make_move(self):
        current_state = self.states_tree

        # przejscie do nastepnego stanu na drzewie po ruchu przeciwnika
        if not self.game.grid.is_empty():
            for successor in self.states_tree.successors:
                if successor.grid == self.game.grid:
                    current_state = successor
                    break

        # wybor nastepnego ruchu w drzewie
        next_move = None
        for successor in current_state.successors:
            if current_state.value == successor.value:
                self.game.grid = successor.grid.copy()
                self.states_tree = successor
                break
