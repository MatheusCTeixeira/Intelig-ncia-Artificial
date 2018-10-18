import sys

sys.path.append("..")


from model_Puzzle8Pieces_Benchmark import BFS_solution
from model_Puzzle8Pieces_Benchmark import E0
from model_Puzzle8Pieces_Benchmark import encoding

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

from PyQt5.QtChart import QBarSeries, QBarSet, QChart, QChartView, QBarCategoryAxis

#--------------------------------------------------------------------------#


class Piece(QLabel):
    """ Representa uma peça no tabuleiro """
    matrix_piece = []

    def __init__(self, text, position, board, pieces):
        super().__init__()
        super().setText(text)

        self.position = position
        self.board = board
        self.pieces = pieces

        print(self.board)

        #i, j = self.position
        #while len(self.matrix_piece) <= i:
        #    self.matrix_piece.append([])
#
        #while len(self.matrix_piece[i]) <= j:
        #    self.matrix_piece[i].append(self)

    def swap_text(self, lbl1, lbl2):
        text = lbl1.text()
        lbl1.setText(lbl2.text())
        lbl2.setText(text)
  
    def update_pieces(self):         
        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[0])):
                self.pieces[i][j].setText(str(self.board[i][j]))

    def swap_map(self, pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2

        val = self.board[i1][j1]
        self.board[i1][j1] = self.board[i2][j2]
        self.board[i2][j2] = val

    def mousePressEvent(self, mouse_event):
        """ Processa o evento de click em um peça do tabuleiro """
        i, j = self.position

        if i > 0 and self.board[i - 1][j] == 0:
            self.swap_map(self.position, (i - 1, j))

        elif i + 1 < len(self.board) and self.board[i + 1][j] == 0:
            self.swap_map(self.position, (i + 1, j))

        elif j > 0 and self.board[i][j - 1] == 0:
            self.swap_map(self.position, (i, j - 1))

        elif j + 1 < len(self.board[0]) and self.board[i][j + 1] == 0:
            self.swap_map(self.position, (i, j + 1))

        self.update_pieces()

        for line in self.board:
            for x in line:
                print("%3d" % x, end='')
            print()

        print("---------------------------------------------\n")

#--------------------------------------------------------------------------#

#
#class SolutionManager:
#    """ Esta classe é resposável por controlar a exibição da solução passo a passo """
#
#    def __init__(self, solution):
#        self.solution = solution
#        self.step = 0        
#
#    def step_foward(self):
#        
#
#        if (len(self.solution) + 1 < self.step):
#            self.step += 1
#
#    def step_back(self):
#        if (self.step > 0):
#            self.step -= 1
#
#    def get_step(self):
#        if (self.solution != None and len(self.solution) > self.step):
#            return self.solution[self.step]
#

#--------------------------------------------------------------------------#


class ControlButton(QPushButton):
    """ Representa os buttons para iterar a solução """  

    solution = None  
    step = 0

    def __init__(self, text, action, board, pieces):
        super().__init__()
        super().setText(text)

        self.action = action    #Indica o tipo de ação de cada button
        self.board = board      #Armazenas as peças (como valores lógicos)
        self.pieces = pieces    #Armazenas as peças (como componentes gráficos)

        #self.solution = None    #Representa a solução obtida
        #self.step = 0           #Representa o passo da solução atual
        
    def mouseReleaseEvent(self, event):
        """ Ação de clicar no button """
        if self.action == "solution":
            self.find_solution()
        elif self.action == "foward":
            self.foward()
        elif self.action == "back":
            self.back()

        super().mouseReleaseEvent(event)

    def find_solution(self):
        E0 = encoding(self.board)
        ControlButton.solution = BFS_solution(E0)
        ControlButton.step = 0
        print(self.solution)
            
    def foward(self):
        
        if ControlButton.solution == None:
            return


        step = ControlButton.step
        print(step)
        solution = ControlButton.solution        

        if step < len(solution) - 1:
            ControlButton.step += 1
            step += 1

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = solution[step][i][j]
  

        self.update_pieces()

    def back(self):
        if ControlButton.solution == None:
            return

        step = ControlButton.step
        print(step)
        solution = ControlButton.solution

        if step > 0:
            ControlButton.step -= 1
            step -= 1
        

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = solution[step][i][j]
  

        self.update_pieces()

    def update_pieces(self):         
        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[0])):
                self.pieces[i][j].setText(str(self.board[i][j]))

    def swap_map(self, pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2

        val = self.board[i1][j1]
        self.board[i1][j1] = self.board[i2][j2]
        self.board[i2][j2] = val
#--------------------------------------------------------------------------#


class Game:
    """ Representa a interface do jogo """

    def __init__(self, N):
        app = QApplication([])
        
        self.N = N

        vLayout = QVBoxLayout()
        vLayout.addWidget(QLabel("<h1><center>Quebra-Cabeça N Peças</center></h1>"))
        vLayout.addWidget(self.create_board(self.N))
        vLayout.addWidget(self.create_controls())
        vLayout.addWidget(self.solution_methods())

        hLayout = QHBoxLayout()
        hLayout.addLayout(vLayout)
        hLayout.addWidget(self.draw_result())

        widget = QWidget()
        widget.setLayout(hLayout)
        widget.setStyleSheet("background: white;")
        widget.show()

        app.exec_()

    #--------------------------------------------------------------------------#

    def create_board(self, N):
        """ Cria o tabuleiro """

        self.board = [[a+b*N for a in range(N)] for b in range(N)]
        self.pieces = [[] for b in range(N)]
        piece_size = 50

        pane = QWidget()
        pane.setStyleSheet("border: 1px solid black;")

        grid = QGridLayout()
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                piece = Piece(str(self.board[i][j]), (i, j), self.board, self.pieces)
                piece.setAlignment(QtCore.Qt.AlignCenter)
                piece.setFont(QFont("source code pro", 20))
                piece.setFixedSize(piece_size, piece_size)
                piece.setLineWidth(2)
                piece.setStyleSheet("border: 1px solid red;\
                                     background: yellow;   \
                                     border-radius: 4px;")
                                     
                self.pieces[i].append(piece)                                     
                grid.addWidget(piece, i, j)

        pane.setLayout(grid)
        return pane

    def solution_methods(self):
        """ Adiciona as opções de soluções utilizando IA """

        self.cbbMethods = QComboBox()
        self.cbbMethods.addItems(["BFS", "DFS Iter.", "DFS Recr."])

        pane = QWidget()

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Método de solução: "))

        hbox.addWidget(self.cbbMethods)

        pane.setLayout(hbox)

        return pane

    #--------------------------------------------------------------------------#

    def create_controls(self):
        """ Itera entre os passos que levam a solução (semelhante a depurar a solução) """

        pane = QWidget()

        hbox = QHBoxLayout()
        ControlButton.board = self.board
        hbox.addWidget(ControlButton("<<",          "back",     self.board, self.pieces))
        hbox.addWidget(ControlButton("Solucionar",  "solution", self.board, self.pieces))
        hbox.addWidget(ControlButton(">>",          "foward",   self.board, self.pieces))
        pane.setLayout(hbox)
    
        return pane

    #--------------------------------------------------------------------------#

    def draw_result(self):
        """ Exibe os resultados para comparação entre os métodos """

        names = ["BFS", "DFS Iter.", "DFS Recr."]

        serie = QBarSeries()
        for k in range(len(names)):
            sett = QBarSet(names[k])
            for i in range(1, 3 + 1):
                sett.append(i)
            serie.append(sett)

        axis = QBarCategoryAxis()
        axis.append("Duração")
        axis.append("Profundidade")
        axis.append("Largura")

        chart = QChart()
        chart.addSeries(serie)
        chart.setAxisX(axis)
        chart.setTitle("Comparação entre os métodoss")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        chart_view = QChartView(chart)
        chart_view.setMinimumWidth(550)
        chart_view.setMaximumWidth(600)
        chart_view.setMaximumHeight(600)

        return chart_view

#--------------------------------------------------------------------------#


game = Game(3)
