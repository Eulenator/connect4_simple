class Connect4:

    def __init__(self):
        self.numberOfColumns = 7
        self.numberOfLines = 6
        self.empty_field = '  '
        self.board = [ [ self.empty_field for _ in range( self.numberOfColumns)] for _ in range(self.numberOfLines) ]

    def visualize_board(self):
        for i, line in enumerate(self.board):
            # Printing the line separators
            print("-" * self.numberOfColumns * 4)
            # Printing the line
            print(*line, sep=' |')

    def is_available(self, line, column):
        if line[column] == self.empty_field:
            return True
        return False

    def player_choice(self, current_player):
        choice = int(input("please " + current_player + " select an empty field between 0 and 6 : "))
        while self.board[0][choice] != self.empty_field:
            choice = int(input("column already full: Please re-choose between 0 and 6 : "))
        return choice

    def player_input(self):
        player_1 = input("Pick a color 'R' or 'Y' ")
        while True:
            if player_1.upper() == 'R':
                player_2='Y'
                print("you have choosen " + player_1 + ". Player 2 will be " + player_2)
                return player_1.upper(),player_2
            elif player_1.upper() == 'Y':
                player_1='R'
                print("you have choosen " + player_1 + ". Player 2 will be " + player_2)
                return player_1.upper(),player_2
            else:
                player_1 = input("please pick a color 'R' or 'Y' ")

    def check_lines(self, marker, board=None):
        if board is None:
            board=self.board
        for line in board:
            for i in range(0,len(line)):
                if i < len(line) - 3:
                    if line[i] == line[i+1] == line[i+2] == line[i+3] == " " + marker:
                        return True

    def check_diagonals(self, marker):
        diagonals = []
        for i, line in enumerate(self.board):
            for idx, item in enumerate(line):
                if item == ' ' + marker:
                    diagonals.append(int(str(i)+str(idx)))

        for item in diagonals:
            if int(item) + 11 in diagonals and int(item) + 22 in diagonals and int(item) + 33 in diagonals:
                return True

        for item in reversed(diagonals):
            if int(item) - 9 in diagonals and int(item) - 18 in diagonals and int(item) - 27 in diagonals:
                return True

    def create_reversed_board(self):
        reversed_board = []
        for line in self.board:
            for index, item in enumerate(line):
                if len(reversed_board) > index:
                    reversed_board[index].append(item)
                else:
                    reversed_board.append([])
                    reversed_board[index].append(item)
        return reversed_board

    def play(self, playercolumn, marker):
        for item in reversed(self.board):
            if self.is_available(item, playercolumn):
                item[playercolumn] = " " + marker
                return True
        return False

c = Connect4()

game = True
while game:
    player_marker_1, player_marker_2 = c.player_input()
    c.visualize_board()
    finished = False
    number_of_rounds = 1
    while not finished:
        if number_of_rounds % 2 == 0:
            currentPlayer = "Reggie"
            marker = player_marker_1
        else:
            currentPlayer = "Johny"
            marker = player_marker_2
        position = c.player_choice(currentPlayer)
        if not c.play(position, marker):
            print(f"Column {position} full")

        reversed_board = c.create_reversed_board()
        if c.check_lines(marker) or c.check_lines(marker, reversed_board) or c.check_diagonals(marker):
            finished = True
            c.visualize_board()
            print(f"Game won by {currentPlayer}")
            
            #start new game
            replay = input("play again (Y/N) ? ")
            if replay.lower() == 'n':
                game = False
                print("game ended!!")
            else:
                c = Connect4()
            break
        c.visualize_board()
        number_of_rounds += 1