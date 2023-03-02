from easyAI import AI_Player,Negamax
from TwoPlayerGame_Controller import *
from easyAI.Player import Human_Player

class GameController(TwoPlayerGame):
    def __init__(self,players,game_board):
        self.possible_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],[3, 5, 7]]
        self.players = players
        self.current_player = 1
        self.board = game_board

    def possible_moves(self):
        # print("Possible_moves",[a+1 for a,b in enumerate(self.board) if b==0])
        return [a+1 for a,b in enumerate(self.board) if b==0]

    def make_move(self, move):
        self.board[int(move)-1] = self.current_player

    def loss_condition(self):
        return any([all([(self.board[i-1]==self.opponent_index)
                         for i in combination]) for combination in self.possible_combinations])

    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    def show(self):
        print('\n'.join([' '.join([['.','O','X'][self.board[3*j+i]]
                                   for i in range(3)]) for j in range(3)]))

        for count, possible_set in enumerate(self.possible_combinations):
            if all([(self.board[i-1]) == 2 for i in possible_set]) :
                print("\n -- ํYOU LOSE --")
                return 'AI'
            elif all([(self.board[i-1]) == 1 for i in possible_set]) :
                print("\n --- ํYOU WIN ---")
                return 'PLAYER'
            else:
                if 0 not in self.board and count+1 == len(self.possible_combinations):
                    print('\n ---- TIE ----')
                    return 'TIE'

    def get_board(self):
        return self.board

    def scoring(self):
        # print("scoring",-100 if self.loss_condition() else 0)
        return -100 if self.loss_condition() else 0

class Start:
    def start_game(self,game_board,negamax_level):
        algorithm = Negamax(negamax_level)
        # after_ai_board = GameController([Human_Player(), AI_Player(algorithm)], game_board).play()
        # return after_ai_board
        return  GameController([Human_Player(), AI_Player(algorithm)], game_board).play()

# if __name__ == '__main__':
#     algorithm = Negamax(5)
#     GameController([Human_Player(),AI_Player(algorithm)]).play()
