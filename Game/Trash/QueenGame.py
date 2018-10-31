
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from enum import Enum

class PieceType(Enum):
    """ Este enum identifica o tipo de cada peça, isto é,
        se é ou não um rainha 
    """
    EMPTY = 0
    QUEEN = 1

class Piece(QPushButton):
    """ Esta classe representa uma peça graficamente """
    QUEEN_ICON = None
    EMPTY_ICON = None

    column_button = []

    def __init__(self, position, map):
        super().__init__()

        self.QUEEN_ICON = QIcon("./Resource/queen.png")
        self.EMPTY_ICON = QIcon()

        self.position = position
        self.map = map

        # Mantém os button que estam na mesma coluna
        # na mesma lista
        i, j = self.position
        while len(self.column_button) <= j:
            self.column_button.append([])

        self.column_button[j].append(self)        

    def refresh(self):
        """ Atualiza as peças que estão na mesma coluna """
        i, j = self.position

        for x in range(len(self.column_button[j])):            
            if self.map[x][j] == PieceType.EMPTY:
                self.column_button[j][x].setIcon(self.EMPTY_ICON)
            else:
                self.column_button[j][x].setIcon(self.QUEEN_ICON)

    def mousePressEvent(self, mouseEvent):        
        """ Atualiza o tipo de cada peça no mapa """
        i, j = self.position
        self.map[i][j] = PieceType.QUEEN
        
        for x in [val for val in range(len(self.map)) if val != i]:
            self.map[x][j] = PieceType.EMPTY

        self.refresh()

        
        for line in self.map:
            print([x.value for x in line])

        print("=====================================\n")
            


class QueenGame:
    " Esta classe representa o jogo"

    # @N é a ordem do jogo
    def __init__(self, N):
        self.N = N
        self.map = [[PieceType.EMPTY for col in range(self.N)] for lin in range(self.N)]

        app = QApplication([])

        widget = self.draw_board()
        widget.show()
        app.exec_()

    def draw_board(self):
        for x in range(self.N):
            self.map[0][x] = PieceType.QUEEN


        grid = QGridLayout()
        grid.setSpacing(4)
        for i in range(self.N):
            for j in range(self.N):
                piece = Piece((i, j), self.map)
                
                if self.map[i][j] == PieceType.QUEEN:
                    piece.setIcon(QIcon("./Resource/queen.png"))
                else:
                    piece.setIcon(QIcon())
                
                piece.setStyleSheet("background: white;")
                piece.setIconSize(QSize(40, 40))
                piece.setFixedSize(QSize(50, 50))
                grid.addWidget(piece, i, j)

        pane = QWidget()
        pane.setLayout(grid)

        return pane
        

                
game = QueenGame(8)
        
