
from enum import Enum

from copy import deepcopy

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QComboBox, QSlider
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BoardMode(Enum):
    EDIT_MODE = 1
    PLAY_MODE = 2
    UNSTABLE_MODE = 3

class Board(QWidget):
    def __init__(self, max_order):        
        self.board_size = 300
        self.max_order = max_order
        self.current_order = max_order
        self.mode = BoardMode.PLAY_MODE
        self.unused_values = []
        self.max_tolerable_solution_depth = 8

        self.logic_board = self.create_logic_board(self.current_order)
        self.graphic_board = self.create_graphic_board()
        self.set_final_state()
        self.graphic_edit_board = self.create_graphic_edit_board()
        self.all_widgets = {}

    #-------------------------------------------------------------------------------#

    def create_graphic_board(self):
        buttons = []
        for i in range(self.max_order):
            buttons.append([])
            for j in range(self.max_order): 
                valid_button = i < self.current_order and j < self.current_order

                button = QPushButton()     
                button.setFixedSize(self.board_size/self.current_order, self.board_size/self.current_order)    
                button.setVisible(valid_button)    
                    
                button.clicked.connect(lambda arg, coord=(i, j): self.piece_click(coord))
                button.setText(str(i * self.current_order + j) if valid_button else " ")
                buttons[i].append(button)

        
        return buttons

    #-------------------------------------------------------------------------------#

    def create_graphic_edit_board(self):
        comboboxs = []
        for i in range(self.max_order):
            comboboxs.append([])
            for j in range(self.max_order): 
                combobox = QComboBox()
                combobox.setFixedSize(self.board_size / self.current_order, self.board_size / self.current_order)
                combobox.setVisible(False)
                combobox.currentIndexChanged.connect(\
                    lambda arg, param=(i, j):\
                        self.select_piece_value_edit_mode(param)\
                )

                comboboxs[i].append(combobox)

        return comboboxs

    #-------------------------------------------------------------------------------#

    def create_logic_board(self, order):
        board = [[i *order + j for j in range(order)]\
                               for i in range(order)]

        return board

    #-------------------------------------------------------------------------------#

    def update_graphic_board(self):        
        self.update_graphic_board_text()     
        self.update_graphic_board_size()
        
        self.update_edit_graphic_board_text()
        self.update_edit_graphic_board_size()

        self.update_board_visibility()

    #-------------------------------------------------------------------------------#        

    def update_board_visibility(self):
        for i in range(self.max_order):                
            for j in range(self.max_order):                          
                self.graphic_board[i][j]\
                    .setVisible(i < self.current_order and j < self.current_order and self.mode == BoardMode.PLAY_MODE)

                self.graphic_edit_board[i][j]\
                    .setVisible(i < self.current_order and j < self.current_order and self.mode == BoardMode.EDIT_MODE)

    #-------------------------------------------------------------------------------#

    def update_graphic_board_text(self):
        if self.mode != BoardMode.PLAY_MODE:  
            return

        for i in range(self.current_order):                
            for j in range(self.current_order):    
                self.graphic_board[i][j]\
                    .setText(str(self.logic_board[i][j]))

    #-------------------------------------------------------------------------------#

    def update_graphic_board_size(self):
        if self.mode != BoardMode.PLAY_MODE:  
            return

        new_size = self.board_size / self.current_order
        for i in range(self.current_order):                
            for j in range(self.current_order):    
                self.graphic_board[i][j]\
                    .setFixedSize(new_size, new_size)

    #-------------------------------------------------------------------------------#    

    def update_edit_graphic_board_text(self):
        if self.mode != BoardMode.EDIT_MODE:
            return

        self.mode = BoardMode.UNSTABLE_MODE
        
        for i in range(self.current_order):                
            for j in range(self.current_order):   
                    self.graphic_edit_board[i][j]\
                        .setCurrentText(str(self.logic_board[i][j]))  

        self.mode = BoardMode.EDIT_MODE

    #-------------------------------------------------------------------------------#

    def update_edit_graphic_board_size(self):
        if self.mode != BoardMode.EDIT_MODE:
            return        
        
        new_size = self.board_size / self.current_order
        for i in range(self.current_order):                
            for j in range(self.current_order):    
                self.graphic_edit_board[i][j]\
                    .setFixedSize(new_size, new_size)       

    #-------------------------------------------------------------------------------#

    def set_order(self, order):
        if order > self.max_order:
            print("Invalid order")
            return
        
        self.current_order = order
        self.logic_board = self.create_logic_board(order)
        self.set_final_state()
       
        self.update_graphic_board()

    #-------------------------------------------------------------------------------#

    def piece_click(self, coord):
        if self.mode != BoardMode.PLAY_MODE:
            return           
             
        i, j = coord   
        current_value = self.logic_board[i][j]     

        if i - 1 >= 0 and self.logic_board[i - 1][j] == 0: #up
            self.logic_board[i][j] = self.logic_board[i - 1][j]
            self.logic_board[i - 1][j] = current_value
        elif i + 1 < self.current_order and self.logic_board[i + 1][j] == 0: #down
            self.logic_board[i][j] = self.logic_board[i + 1][j]
            self.logic_board[i + 1][j] = current_value
        elif j - 1 >= 0 and self.logic_board[i][j - 1] == 0: #left
            self.logic_board[i][j] = self.logic_board[i][j - 1]
            self.logic_board[i][j - 1] = current_value

        elif j + 1 < self.current_order and self.logic_board[i][j + 1] == 0: #right
            self.logic_board[i][j] = self.logic_board[i][j + 1]
            self.logic_board[i][j + 1] = current_value

        self.update_graphic_board()

    #-------------------------------------------------------------------------------#

    def widget_board(self):
        grid_board = QGridLayout()          
        grid_board.setSpacing(0)      
        for i in range(self.current_order):
            for j in range(self.current_order):
                grid_board.addWidget(self.graphic_board[i][j], i, j)
                grid_board.addWidget(self.graphic_edit_board[i][j], i, j)

        board_widget = QWidget()
        board_widget.setLayout(grid_board)

        return board_widget

    #-------------------------------------------------------------------------------#

    def enable_edit_mode(self, value):        
        self.mode = BoardMode.UNSTABLE_MODE

        valid_values = [v for v in range(self.current_order ** 2)]
        for i in range(self.current_order):
            for j in range(self.current_order):                
                self.graphic_edit_board[i][j].clear()
                self.graphic_edit_board[i][j].addItems([str(vl) for vl in valid_values])
                self.graphic_edit_board[i][j].setCurrentText(str(self.logic_board[i][j]))

        self.mode = BoardMode.EDIT_MODE if value else BoardMode.PLAY_MODE
        self.update_graphic_board()
        
    #-------------------------------------------------------------------------------#

    def select_piece_value_edit_mode(self, coord):        
        if self.mode == BoardMode.UNSTABLE_MODE:
            return
        
        i, j = coord                
        value = self.graphic_edit_board[i][j].currentText()     

        self.mode = BoardMode.UNSTABLE_MODE        
        
        (i_to_subs, j_to_subs), not_used_value = self.find_unsigned_value_and_point(value, coord)

        self.graphic_edit_board[i_to_subs][j_to_subs]\
            .setCurrentText(str(not_used_value))

        self.logic_board[i_to_subs][j_to_subs] = not_used_value
        self.logic_board[i][j] = int(value)        

        self.mode = BoardMode.EDIT_MODE   

    #-------------------------------------------------------------------------------#

    def find_unsigned_value_and_point(self, value, coord):
        i, j = coord
        i_to_subs, j_to_subs = -1, -1

        valid_values = [x for x in range(self.current_order ** 2)]
        for _i in range(self.current_order):
            for _j in range(self.current_order): 
                cm_value = int(self.graphic_edit_board[_i][_j].currentText())
                if cm_value in valid_values:
                    valid_values.remove(cm_value)
                
                if cm_value == int(value) and not (_i == i and _j == j):
                    i_to_subs, j_to_subs = _i, _j 

        #assert
        if len(valid_values) != 1:            
            print("Error: inconsistency at "  +\
                  self.__class__.__name__ + "." +\
                  self.find_unsigned_value_and_point.__name__)

            exit(1)

        return ((i_to_subs, j_to_subs), valid_values[0]) 

    #-------------------------------------------------------------------------------#

    def graphic_board_mode(self):        
        play_mode_btn = QPushButton("PLAY MODE")
        play_mode_btn.clicked.connect(lambda pq, value = False: self.enable_edit_mode(value))
        
        edit_mode_btn = QPushButton("EDIT MODE")
        edit_mode_btn.clicked.connect(lambda pq, value = True: self.enable_edit_mode(value))       

        h_layout = QHBoxLayout()
        h_layout.addWidget(play_mode_btn)
        h_layout.addWidget(edit_mode_btn)

        component = QWidget()
        component.setLayout(h_layout)

        return component

    #-------------------------------------------------------------------------------#

    def get_logic_board(self):
        return self.logic_board

    #-------------------------------------------------------------------------------#

    def set_logic_board(self, board):
        len_of_board = len(board)
        if len_of_board > self.max_order:
            print("len is too big")
            exit(-1)

        self.current_order = len_of_board
        self.logic_board = board
        self.update_graphic_board()

    #-------------------------------------------------------------------------------#

    def graphic_order(self):
        cross = lambda i: str(i) + "x" + str(i)
        combobox = QComboBox()        
        combobox.addItems([cross(x) for x in range(3, self.max_order + 1)])    
        combobox.setCurrentIndex(self.current_order - 3)    
        combobox.currentIndexChanged\
                .connect(lambda arg, cbb = combobox:self.process_graphic_order(cbb))        
        
        return combobox

    #-------------------------------------------------------------------------------#

    def process_graphic_order(self, cbb):
        new_order = int(cbb.currentText()[0])
        self.set_order(new_order)  

    #-------------------------------------------------------------------------------#

    def set_final_state(self):
        self.final_state = deepcopy(self.logic_board)
 
    #-------------------------------------------------------------------------------#

    def get_final_state(self):
        return self.final_state

    #-------------------------------------------------------------------------------#

    def graphic_final_state(self):
        button = QPushButton()
        button.setText("&Set &Final &State")
        button.clicked.connect(lambda arg: self.set_final_state())
    
        return button
    
    #-------------------------------------------------------------------------------#

    def graphic_select_solution_method(self):
        combobox = QComboBox()
        combobox.addItems(["Selecione o método de busca","BFS", "DFS Iterativo", "DFS Recursivo"])
        combobox.currentTextChanged\
                .connect(lambda arg, method = combobox: self.find_solution(method))

        return combobox

    #-------------------------------------------------------------------------------#
    
    def find_solution(self, method):
        if self.mode == BoardMode.UNSTABLE_MODE:
            return

              
        self.mode = BoardMode.UNSTABLE_MODE      

        method_selected = method.currentText()
        print(method_selected + " " + str(self.max_tolerable_solution_depth))
        print(self.logic_board)
        print(self.final_state)
        method.setCurrentIndex(0)
        self.mode = BoardMode.PLAY_MODE

    #-------------------------------------------------------------------------------#

    def graphic_select_depth(self):
        slider = QSlider()
        slider.setRange(1, 30)
        slider.setValue(self.max_tolerable_solution_depth)
        slider.setOrientation(Qt.Horizontal)
        slider.valueChanged\
              .connect(lambda arg, comp = slider: self.selected_depth(comp))
        
        return slider

    #-------------------------------------------------------------------------------#

    def selected_depth(self, comp):        
        self.max_tolerable_solution_depth = comp.value()

    #-------------------------------------------------------------------------------#

    def graphic_solution_iteraction(self):
        back_step = QPushButton()
        back_step.setIcon(QIcon(BASE_DIR + "/resources/left.png"))
        back_step.clicked.connect(lambda arg: self.back_step_solution())

        begin_step = QPushButton()
        begin_step.setIcon(QIcon(BASE_DIR + "/resources/play.png"))
        begin_step.clicked.connect(lambda arg: self.begin_step_solution())

        foward_step = QPushButton()
        foward_step.setIcon(QIcon(BASE_DIR + "/resources/right.png"))
        foward_step.clicked.connect(lambda arg: self.foward_step_solution())

        h_layout = QHBoxLayout()
        h_layout.addWidget(back_step)
        h_layout.addWidget(begin_step)
        h_layout.addWidget(foward_step)

        widget = QWidget()
        widget.setLayout(h_layout)
        return widget

    #-------------------------------------------------------------------------------#

    def back_step_solution(self):
        print("back")
    #-------------------------------------------------------------------------------#

    def begin_step_solution(self):
        print("begin")

    #-------------------------------------------------------------------------------#

    def foward_step_solution(self):
        print("foward")

    #-------------------------------------------------------------------------------#

class Main:
    def __init__(self):
        
        app = QApplication([])

        board = Board(9)
        
        vBoxLayout = QVBoxLayout()        
        
        vBoxLayout.addWidget(board.widget_board())
        vBoxLayout.addWidget(board.graphic_final_state())
        vBoxLayout.addWidget(board.graphic_board_mode())
        vBoxLayout.addWidget(board.graphic_order())
        vBoxLayout.addWidget(board.graphic_select_depth())
        vBoxLayout.addWidget(board.graphic_select_solution_method())
        vBoxLayout.addWidget(board.graphic_solution_iteraction())

        window = QWidget()
        window.setWindowTitle("Quebra-Cabeça")
        window.setLayout(vBoxLayout)
        window.show()

        app.exec_()
        
Main()
    
