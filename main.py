from tictactoe import TicTacToe
from minimax_full import FullPlayer, minimax_full, State
from minimax import MinimaxPlayer, minimax
from random_player import RandomPlayer
import time


def test_time():
    state = State()

    start_time = time.time()
    minimax_full(state)
    execution_time = round(time.time() - start_time, 2)
    print(f'Full minimax: {execution_time}s')

    for i in range(1, 10):
        start_time = time.time()
        minimax(state, i)
        execution_time = round(time.time() - start_time, 2)
        print(f'Minimax depth = {i}: {execution_time}s')


def test_1():
    # random vs random

    O_win = 0
    X_win = 0
    draw = 0

    for i in range(100):
        game = TicTacToe()
        
        p1 = RandomPlayer(game, 'O')
        p2 = RandomPlayer(game, 'X')

        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            O_win += 1
        elif game.result == 'X':
            X_win += 1
        else:
            draw += 1
    
    print('Random vs random:')
    print('O: ', O_win)
    print('X: ', X_win)
    print('draw: ', draw)


def test_2():
    # random vs full minimax

    O_win = 0
    X_win = 0
    draw = 0

    states_tree = minimax_full(State())

    for i in range(100):
        game = TicTacToe()
        
        p1 = FullPlayer(game, 'O', states_tree)
        p2 = RandomPlayer(game, 'X')

        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            O_win += 1
        elif game.result == 'X':
            X_win += 1
        else:
            draw += 1
    
    print('Random (O) vs full minimax (X):')
    print('O: ', O_win)
    print('X: ', X_win)
    print('draw: ', draw)


def test_3():
    # full minimax vs full minimax

    O_win = 0
    X_win = 0
    draw = 0

    states_tree = minimax_full(State())

    for i in range(100):
        game = TicTacToe()
        
        p1 = FullPlayer(game, 'O', states_tree)
        p2 = FullPlayer(game, 'X', states_tree)

        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            O_win += 1
        elif game.result == 'X':
            X_win += 1
        else:
            draw += 1
    
    print('Full minimax vs Full minimax:')
    print('O: ', O_win)
    print('X: ', X_win)
    print('draw: ', draw)


def test_4():
    # full minimax vs minimax depth = 4

    O_win = 0
    X_win = 0
    draw = 0

    states_tree = minimax_full(State())

    for i in range(100):
        game = TicTacToe()
        p1 = FullPlayer(game, 'O', states_tree)
        p2 = MinimaxPlayer(game, 'X', 4)
        
        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            O_win += 1
        elif game.result == 'X':
            X_win += 1
        else:
            draw += 1
    
    print('Full minimax (O) vs minimax depth = 4 (X):')
    print('O: ', O_win)
    print('X: ', X_win)
    print('draw: ', draw)


def test_5():
    # random vs minimax depth = 4

    O_win = 0
    X_win = 0
    draw = 0

    for i in range(100):
        game = TicTacToe()
        p1 = RandomPlayer(game, 'O')
        p2 = MinimaxPlayer(game, 'X', 4)
        
        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            O_win += 1
        elif game.result == 'X':
            X_win += 1
        else:
            draw += 1
    
    print('Random (O) vs minimax depth = 4 (X):')
    print('O: ', O_win)
    print('X: ', X_win)
    print('draw: ', draw)


def test_6():
    # minimax depth = 6 vs minimax depth = 2

    depth_2 = 0
    depth_6 = 0
    draw = 0

    for i in range(50):
        game = TicTacToe()
        p1 = MinimaxPlayer(game, 'O', 6)
        p2 = MinimaxPlayer(game, 'X', 2)
        
        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            depth_6 += 1
        elif game.result == 'X':
            depth_2 += 1
        else:
            draw += 1

    for i in range(50):
        game = TicTacToe()
        p1 = MinimaxPlayer(game, 'O', 2)
        p2 = MinimaxPlayer(game, 'X', 6)
        
        while not game.is_finished():
            p1.make_move()
            p2.make_move()

        if game.result == 'O':
            depth_2 += 1
        elif game.result == 'X':
            depth_6 += 1
        else:
            draw += 1
    
    print('minimax depth = 2 vs minimax depth = 6:')
    print('depth = 2: ', depth_2)
    print('depth = 6: ', depth_6)
    print('draw: ', draw)


def main():
    test_time()
    #test_1()
    #test_2()
    #test_3()
    #test_4()
    #test_5()
    #test_6()


if __name__ == "__main__":
    main()