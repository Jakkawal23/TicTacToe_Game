from tkinter import *
from TwoPlayerGame_Controller import *
from AI_Controller import *

class Interface:
    def __init__(self):
        self.board = [0] * 9
        self.board_button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.negamax_level = 5
        window = Tk()
        window.title("Tic-Tac-Toe")

        menubar = Menu(window)
        fileMenu1 = Menu(menubar, tearoff=0)
        fileMenu1.add_command(label="Easy ",command=lambda : self.ai_level(2,"Easy"))
        fileMenu1.add_command(label="Medium",command=lambda : self.ai_level(5,"Medium"))
        fileMenu1.add_command(label="Hard",command=lambda : self.ai_level(10,"Hard"))

        fileMenu2 = Menu(menubar, tearoff=0)
        fileMenu2.add_command(label="6302XXXX นายจักรวาล ภูเลื่อมใส")
        fileMenu2.add_command(label="6302XXXX นายวรเมธ สยาม")
        fileMenu2.add_command(label="6302XXXX นางสาวพัชรวรินทร์ จินกลาง")

        menubar.add_cascade(label="Level", menu=fileMenu1)
        menubar.add_cascade(label="Member", menu=fileMenu2)

        window.config(menu=menubar)

        self.label = Label(text="Tic-Tac-Toe", font=('consolas', 40))
        self.label.pack(side="top")

        self.frame = Frame(window)
        self.frame.pack()

        self.board_interface()

        reset_button = Button(text="restart", font=('consolas', 20), command=lambda : self.new_game())
        reset_button.pack(side="top")

        self.level_label = Label(text="Medium Level", font=('consolas', 20))
        self.level_label.pack(side="top")

        window.mainloop()

    def ai_level(self,level,label):
        self.negamax_level = level
        self.new_game()
        self.level_label.config(text=label+" Level")

    def new_game(self):
        self.board = [0] * 9
        self.label.config(text="Tic-Tac-Toe")
        for row in range(3):
            for column in range(3):
                self.board_button[row][column]['text'] = ""
                self.board_button[row][column].config(bg="#F0F0F0")

    def board_interface(self):

        button_index = 0
        for row in range(3):
            for column in range(3):
                button_index += 1
                self.board_button[row][column] = Button(self.frame,text="", font=('consolas', 40), width=5, height=2,
                                              command=lambda row=row, column=column, button_index=button_index : self.to_move(row, column,button_index))
                self.board_button[row][column].grid(row=row, column=column)

    def show_interface(self):
        # x_action = []
        # o_action = []
        button_index = 0
        # self.check_winner()
        for row in range(3):
            for column in range(3):
                if self.board[button_index] == 1 :
                    self.board_button[row][column]['text'] = "X"
                    self.board_button[row][column].config(bg="#40dde6")
                elif self.board[button_index] == 2 :
                    self.board_button[row][column]['text'] = "O"
                    self.board_button[row][column].config(bg="#ff6c5f")
                else :
                    pass
                button_index += 1

    def check_winner(self):
        win_color = "#279b37"
        print("self.action = ",str(self.action))
        if self.action == 'AI':
            win_color = "#fc1e1e"
            self.label.config(text="AI WIN")
        if self.action == 'PLAYER':
            win_color = "#3ebbfa"
            self.label.config(text="PLAYER WIN")

        for row in range(3):
            if self.board_button[row][0]['text'] == self.board_button[row][1]['text'] == self.board_button[row][2]['text'] != "":
                self.board_button[row][0].config(bg=win_color)
                self.board_button[row][1].config(bg=win_color)
                self.board_button[row][2].config(bg=win_color)
                return True

        for column in range(3):
            if self.board_button[0][column]['text'] == self.board_button[1][column]['text'] == self.board_button[2][column]['text'] != "":
                self.board_button[0][column].config(bg=win_color)
                self.board_button[1][column].config(bg=win_color)
                self.board_button[2][column].config(bg=win_color)
                return True

        if self.board_button[0][0]['text'] == self.board_button[1][1]['text'] == self.board_button[2][2]['text'] != "":
            self.board_button[0][0].config(bg=win_color)
            self.board_button[1][1].config(bg=win_color)
            self.board_button[2][2].config(bg=win_color)
            return True

        elif self.board_button[0][2]['text'] == self.board_button[1][1]['text'] == self.board_button[2][0]['text'] != "":
            self.board_button[0][2].config(bg=win_color)
            self.board_button[1][1].config(bg=win_color)
            self.board_button[2][0].config(bg=win_color)
            return True

        elif self.empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    self.board_button[row][column].config(bg="#ffc168")
            return "Tie"

        else:
            return False


    def empty_spaces(self):

        spaces = 9

        for row in range(3):
            for column in range(3):
                if self.board_button[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def on_move(self):
        pass

    def is_not_select(self,button_index):
        for i in range(len(self.board)):
            if(self.board[i] == 1 or self.board[i] == 2):
                if(button_index == i+1):
                    return False
        return True

    def to_move(self, row, column,button_index):
        if(self.is_not_select(button_index)):
            self.label.config(text="Tic-Tac-Toe")
            TwoPlayerGame.move_index = str(button_index)
            self.action = Start.start_game(Start, self.board,self.negamax_level)
            self.show_interface()
            self.check_winner()
        else:
            if self.action not in ['AI', 'PLAYER', 'TIE']:
                self.label.config(text="Choose again")

if __name__ == '__main__':
    Interface()