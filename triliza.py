import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class TicTacToeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.cells = []
        
        for row in range(3):
            row_cells = []
            for col in range(3):
                cell = QLineEdit()
                cell.setAlignment(Qt.AlignCenter)
                font = cell.font()
                font.setPointSize(24)
                font.setBold(True)
                cell.setFont(font)
                self.grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)
            
        main_layout.addLayout(self.grid_layout)
        self.status_label = QLabel("Play")
        self.status_label.setAlignment(Qt.AlignCenter)
        status_font = self.status_label.font()
        status_font.setPointSize(16)
        self.status_label.setFont(status_font)
        main_layout.addWidget(self.status_label)
        
        self.check_button = QPushButton("check")
        self.check_button.clicked.connect(self.check_game)
        main_layout.addWidget(self.check_button)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(self.reset_button)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Τρίλιζα")
        self.resize(300, 350)
        self.show()

    def check_game(self):
        board = []
        for row in range(3):
            board_row = []
            for col in range(3):
                val = self.cells[row][col].text().strip().upper()
                board_row.append(val)
            board.append(board_row)
            
        for row in range(3):
            for col in range(3):
                val = board[row][col]
                if val != "" and val != "X" and val != "O":
                    self.status_label.setText("Invalid Input")
                    return

        winner = None

        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
                winner = board[row][0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
                winner = board[0][col]

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            winner = board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            winner = board[0][2]

        if winner:
            self.status_label.setText(f"{winner} won")
        else:
            self.status_label.setText("Play")

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].clear()
        self.status_label.setText("Play")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToeGUI()
    sys.argv[0] = "tictactoe"
    sys.exit(app.exec_())
