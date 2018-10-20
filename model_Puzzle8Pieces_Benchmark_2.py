
import DFSIterative
import DFSRecursive
import BFS

import math
import time
import random
import copy

import argparse

import sys
import math


N = 5 # Ordem do tabuleiro

def encoding(E):
    mask = 2 ** N - 1
    value = 0
    for line in E:
        for v in line:
            value = value << N
            value = value | (mask & v)         
            
    return value

def decoding(value):
    vl = value
    mask = 2 ** N - 1
    mask_bitsize = math.ceil(math.log2(N**2))
    E = []
    for j in range(0, N):
        E.insert(0, [])
        for i in range(0, N):
            E[0].insert(0, (mask & vl))
            vl = vl >> mask_bitsize

    return E

#--Estado inicial
E0 =  encoding([ [1,2,3] ,  [4,0,6] , [7,5, 8]])

#--Estado final
Eobj = encoding([ [0,1,2] ,  [3,4,5] , [6,7, 8]])

#-- Procura a posição atual
def posicaoAtual(Et):       
    mask = 2 ** N - 1
    mask_bitsize = math.ceil(math.log2(N**2))
    for i in range(0, N ** 2):
        if (Et >> (i * mask_bitsize)) & mask == 0:      
            return ((N - 1) - math.floor(i  / N), (N - 1) - (i  % N))
        
#------------------------------------------------


#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    acoes_possiveis = []

    posicao = posicaoAtual(Et)
    
    lin, col = posicao
   
    if lin > 0:
        acoes_possiveis.append("up")

    if lin < N - 1:
        acoes_possiveis.append("down")

    if col > 0: 
        acoes_possiveis.append("left")

    if col < N - 1: 
        acoes_possiveis.append("right")

    return acoes_possiveis
#------------------------------------------------



#--Troca duas posições
def trocaPosicao(Et, p0, p1):
    Etemp = decoding(Et)

    l0, c0 = p0
    l1, c1 = p1

    # swap
    Etemp[l0][c0], Etemp[l1][c1] = Etemp[l1][c1], Etemp[l0][c0]

    return encoding(Etemp) 
    
#------------------------------------------------



#--Executar ações
def executarAcao( Et, acao):
    posAt = posicaoAtual(Et)
    lin, col = posAt

    if (acao == "up"):
        lin = lin - 1
    elif (acao == "down"):
        lin = lin + 1
    elif (acao == "left"):
        col = col - 1
    elif (acao == "right"):
        col = col + 1

    Et = trocaPosicao(Et, posAt, (lin, col))

    return Et
   
#------------------------------------------------

#--Compara igualdade de estados
# **** É possivel associar um inteiro a cada estado e
# **** assim a comparação seria direta
def cmpEstados(Ea, Eb):       
    return Ea == Eb
#------------------------------------------------

def funcaoHash(Et):
    return Et % 50

#------------------------------------------------

def randomize_initial_state(state_objective, step):    
    
    solution = []
    initial_state = state_objective
    states_already_visited = [state_objective]

    while len(solution) < step:
        #List all possible actions
        acoes = listarAcoes(initial_state)
        
        #Choice a possibility randolly from the possible actions
        action = acoes[random.randint(0, len(acoes) - 1)]
                
        temp_state = executarAcao(initial_state, action)

        #Add the step if the state is new
        if states_already_visited.count(temp_state) == 0:
            solution.append(action)
            initial_state = temp_state
            states_already_visited.append(temp_state)
        
    print("initial state: %s" %str(decoding(initial_state)))
    print("solution: %s" %str(solution))
    return initial_state


def BFS_solution(E0):
    # print("____________________________________________________")

    busca = BFS.BFS_algorithmcs(list_action_function = listarAcoes,       \
                                execute_action_function = executarAcao,   \
                                hash_function = funcaoHash,               \
                                cmp_function = cmpEstados)
    
    # print("BFS solution: ")

    solution = busca.BFS(E0, Eobj)
    solution.E0 = decoding(solution.E0)
    solution.Ef = decoding(solution.Ef)
    solution.states = [decoding(x) for x in solution.states]

    # print(solution.actions)
    # print(solution.states)
    
    return solution.states

###########################################################################################  
##                                      Test                                             ##
## Ex = [[  0,  1,  2,  3,  4],\                                                         ##                                                                                   
##        [  5,  6,  7,  8,  9],\                                                        ##                                                
##        [ 10, 11, 12, 13, 14],\                                                        ##                                                
##        [ 15, 16, 17, 18, 19],\                                                        ##                                                
##        [ 20, 21, 22, 23, 24] \                                                        ##                                                
##       ]                                                                               ##
##                                                                                       ##
##  Eenc = encoding(Ex)                                                                  ##
##  print(bin(Eenc))                                                                     ##
##  print(decoding(Eenc))                                                                ##
##  for i in range(0, 25):                                                               ##
##      p2 = (math.floor(i/5), i % 5)                                                    ##
##      print(p2)                                                                        ##
##      Eenc = trocaPosicao(Eenc, posicaoAtual(Eenc), p2)                                ##
##      print(listarAcoes(Eenc))                                                         ##
###########################################################################################