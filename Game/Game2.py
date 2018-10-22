import sys

sys.path.append("..")


from algoritmos_de_busca_solucao import BFS_solution
from algoritmos_de_busca_solucao import DFS_Iter_solution
from algoritmos_de_busca_solucao import DFS_Recr_solution


#from model_Puzzle8Pieces_Benchmark import E0
#from model_Puzzle8Pieces_Benchmark import encoding

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


from PyQt5.QtChart import QBarSeries, QBarSet, QChart, QChartView, QBarCategoryAxis

from random import randint

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.patches as mpatches

import numpy as np

import time


#--------------------------------------------------------------------------#
# Descrição: Esta classe representa as peças do tabuleiro
#            em termos gráficos, ie, componentes GUI
#
class Piece(QLabel):
    """ Representa uma peça no tabuleiro """
    matrix_piece = []

    def __init__(self, position, board, pieces):
        super().__init__()        

        self.position = position
        self.board = board
        self.pieces = pieces        

    def swap_text(self, lbl1, lbl2):
        text = lbl1.text()
        lbl1.setText(lbl2.text())
        lbl2.setText(text)
  
    def update_pieces(self):         
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
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

        print("Tabuleiro: ")
        for line in self.board:
            for x in line:
                print("%3d" % x, end='')
            print()

        print("-" * 60)







#--------------------------------------------------------------------------#
# Descrição: Esta classe representa os componentes de controle da solução
#            permitindo avançar, recuar e buscar a solução do estado atual
#
class ControlButton(QPushButton):
    """ Representa os buttons para iterar a solução """  

    solution = None  # A solução é comum a todas os três buttons de controle
    step = 0         # O progresso atual da solução

    def __init__(self, text, action, board, pieces, method, series):
        super().__init__()
        super().setText(text)

        self.action = action     #Indica o tipo de ação de cada button
        self.board = board       #Armazenas as peças (como valores lógicos)
        self.pieces = pieces     #Armazenas as peças (como componentes gráficos)
        self.method = method     #O método de solução escolhido
        self.series = series      #As barras gráficas
        
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

        selected_method = str(self.method.currentText())
        print("Método de busca : " + selected_method)

        estado_atual = self.board
        ControlButton.step = 0
        solution = None
        if selected_method == "BFS":
            solution = BFS_solution(estado_atual)
        elif selected_method == "DFS Iter.":
            solution = DFS_Iter_solution(estado_atual)
        elif selected_method == "DFS Recr.":
            solution = DFS_Recr_solution(estado_atual)
      
        self.series[selected_method][0] = solution.duration
        self.series[selected_method][1] = solution.deepth
        self.series[selected_method][2] = solution.width
        
        
        ControlButton.solution = solution.states

        # ----------------------- Console -----------------------
        if len(self.solution) == 0: #Ocorre quando a profundidade é limitada
            print("Não há solução")
            print(" " * 5 + "-" * 12)
        else:
            print("Solução encontrada: ")
            for i in range(len(self.solution)):
                temp = self.solution[i]
                print(" " * 5 + str(i).rjust(2, ' ') + " - " + str(temp))
            print("-" * 60)
            

    def foward(self):
        
        if ControlButton.solution == None or len(ControlButton.solution) <= 1:
            return

        step = ControlButton.step       
        solution = ControlButton.solution        

        if step < len(solution) - 1:
            ControlButton.step += 1
            step += 1

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = solution[step][i][j]

        self.update_pieces()

        # ----------------------- Console -----------------------
        print("Passo " + str(step) + "/" + str(len(solution) - 1))
        print("-" * 60)


    def back(self):
        if ControlButton.solution == None or len(ControlButton.solution) <= 1:
            return

        step = ControlButton.step       
        solution = ControlButton.solution

        if step > 0:
            ControlButton.step -= 1
            step -= 1        

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = solution[step][i][j]  

        self.update_pieces()

        # ----------------------- Console -----------------------
        print("Passo " + str(step) + "/" + str(len(solution) - 1))
        print("-" * 60)


    def update_pieces(self):         
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.pieces[i][j].setText(str(self.board[i][j]))

    def swap_map(self, pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2

        val = self.board[i1][j1]
        self.board[i1][j1] = self.board[i2][j2]
        self.board[i2][j2] = val



class ChangeLayoutButton(QPushButton):
    def __init__(self, order, board, pieces, series):
        super().__init__()

        self.order = order      #A ordem do tabuleiro
        self.board = board      #O tabuleiro lógico
        self.pieces = pieces    #O tabuleiro gráfico
        self.series = series    #O gráfico
        
    def mouseReleaseEvent(self, event):
        N = int(self.order.currentText()[0]) # "NxN"[0] = N
        
        self.change_board(N)
        self.change_pieces(N)

        self.update_pieces()

        print("Tabuleiro: ")
        for line in self.board:
            for x in line:
                print("%3d" % x, end='')
            print()

        for serie in self.series:
            for i in range(len(self.series[serie])):
                self.series[serie][i] = 0

        print("-" * 60)
    
    def change_board(self, N):
        while len(self.board) < N:
            self.board.append([])

        while len(self.board) > N:
            self.board.pop()

        for line in self.board:
            while len(line) < N:
                line.append(0)
            
            while len(line) > N:
                line.pop()

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = i * N + j

    def change_pieces(self, N):
        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[0])):
                if i < N and j < N:
                    self.pieces[i][j].setVisible(True)
                else:
                    self.pieces[i][j].setVisible(False)

    def update_pieces(self):         
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.pieces[i][j].setText(str(self.board[i][j]))

   


#--------------------------------------------------------------------------#
# Descrição: Esta classe representa o jogo como um todo
#            incluindo o tabuleiro e as peças
class Game:
    """ Representa a interface do jogo """

    def __init__(self, order):
        app = QApplication([])
        
        self.order = order
        self.board_order = 5

        vPlot = self.draw_result()

        vLayout = QVBoxLayout()
        vLayout.addWidget(QLabel("<h1><center>Quebra-Cabeça N Peças</center></h1>"))
        vLayout.addWidget(self.create_board())
        vLayout.addWidget(self.solution_methods())
        vLayout.addWidget(self.create_controls())
        vLayout.addWidget(self.change_layout())

        hLayout = QHBoxLayout()
        hLayout.addLayout(vLayout)
        hLayout.addWidget(vPlot)

        widget = QWidget()
        widget.setLayout(hLayout)
        widget.setStyleSheet("background: white;")
        widget.show()

        app.exec_()

    #--------------------------------------------------------------------------#

    def create_board(self):
        """ Cria o tabuleiro """

        N = self.order
        piece_size = 50

        self.board = [[a+b*N for a in range(N)] for b in range(N)]
        self.pieces = [[] for b in range(self.board_order)]
        self.graphical_board = QGridLayout()
        
        for i in range(self.board_order):
            for j in range(self.board_order):
                piece = Piece((i, j), self.board, self.pieces)
                piece.setText(str(self.board[i][j]) if i < N and j < N else "N")
                piece.setAlignment(QtCore.Qt.AlignCenter)                
                piece.setFixedSize(piece_size, piece_size)
                piece.setLineWidth(2)
                piece.setVisible(True if i < N and j < N else False)
                piece.setStyleSheet("border: 1px solid red;\
                                     background: yellow;   \
                                     font-size:  18px;     \
                                     font-weight: bold;    \
                                     border-radius: 2px;")
                                     
                self.pieces[i].append(piece)    
                self.graphical_board.addWidget(piece, i, j)

        pane = QWidget()
        pane.setStyleSheet("border: 1px solid black;")
        pane.setLayout(self.graphical_board)
        return pane

    def solution_methods(self):
        """ Adiciona as opções de soluções utilizando IA """

        self.cbbMethods = QComboBox()
        self.cbbMethods.addItems(["BFS", "DFS Iter.", "DFS Recr."])

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Método de solução: "))
        hbox.addWidget(self.cbbMethods)

        pane = QWidget()
        pane.setLayout(hbox)

        return pane

    #--------------------------------------------------------------------------#

    def create_controls(self):
        """ Itera entre os passos que levam a solução (semelhante a depurar a solução) """

        ControlButton.board = self.board

        hbox = QHBoxLayout()
        hbox.addWidget(ControlButton("<<",          "back",     self.board, self.pieces, self.cbbMethods, self.series))
        hbox.addWidget(ControlButton("Solucionar",  "solution", self.board, self.pieces, self.cbbMethods, self.series))
        hbox.addWidget(ControlButton(">>",          "foward",   self.board, self.pieces, self.cbbMethods, self.series))
    
        pane = QWidget()
        pane.setLayout(hbox)

        return pane

    #--------------------------------------------------------------------------#

    def change_layout(self):
        """ Muda o layout do tabuleiro """

        #QComboBox -> Indica o layout do tabuleiro
        self.order = QComboBox()
        self.order.addItems(["3x3", "4x4", "5x5"])

        #QChangeLayoutButton -> Mudo o layout do mapa
        button = ChangeLayoutButton(self.order, self.board, self.pieces, self.series)
        button.setText("Alterar")

        hbox = QHBoxLayout()
        hbox.addWidget(self.order)
        hbox.addWidget(button)

        pane = QWidget()
        pane.setLayout(hbox)

        return pane                

    #--------------------------------------------------------------------------#

    def draw_result(self):
        """ Exibe os resultados para comparação entre os métodos """        
        names = ["BFS", "DFS Iter.", "DFS Recr."]

        self.series = {}
        
        
        for name in names:
            self.series.update({name: [0 for x in range(3)]})        

        self.plot = Figure()        
        self.plot.set_animated(True)
        
        self.plot_view = FigureCanvas(self.plot)
       
        self._dynamic_ax = self.plot.subplots()

        red_patch = mpatches.Patch(color='red', label='BFS')
        blue_patch = mpatches.Patch(color='blue', label='DFS Iter.')
        green_patch = mpatches.Patch(color='green', label='DFS Rerc.')

        self.plot.legend(handles=[red_patch, blue_patch, green_patch])
        
        self._timer = self.plot_view.new_timer(500, [(self.update_plot, (), {})])

        self._timer.start()

        return self.plot_view

    def update_plot(self):
        symbol = ["r:", "b--", "g^-"]
        self._dynamic_ax.clear()  

        i = 0
        for serie in self.series:
            self._dynamic_ax.plot(\
                [x for x in range(3)], \
                self.series[serie],\
                symbol[i],\
                label=serie
            )
            i += 1
        
        self._dynamic_ax.figure.canvas.draw()


#--------------------------------------------------------------------------#


game = Game(3)
