
import DFSIterative
import DFSRecursive
import BFS

import math
import time
import random
import copy

import argparse

import sys

def encoding(E):
    value = 0
    mask = 0b1111
    for line in E:
        for v in line:
            value = (value << 4)
            value = value | (mask & v)          
            
    return value

def decoding(value):
    vl = value
    mask = 0b1111
    E = []
    for j in range(0, 3):
        E.insert(0, [])
        for i in range(0, 3):
            E[0].insert(0, (mask & vl))
            vl = vl >> 4

    return E

#--Estado inicial
E0 =  encoding([ [1,2,3] ,  [4,0,6] , [7,5, 8]])

#--Estado final
Eobj = encoding([ [0,1,2] ,  [3,4,5] , [6,7, 8]])

#-- Procura a posição atual
def posicaoAtual(Et):       
    mask = 0b1111
    for i in range(0, 9):
        if (Et >> (i * 4)) & mask == 0:      
            return (2 - math.floor(i  / 3), 2 - (i  % 3))
        
#------------------------------------------------


#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    acoes_possiveis = []

    posicao = posicaoAtual(Et)
    
    lin, col = posicao
   
    if lin > 0:
        acoes_possiveis.append("up")

    if lin < 2:
        acoes_possiveis.append("down")

    if col > 0: 
        acoes_possiveis.append("left")

    if col < 2: 
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

    busca = BFS.BFS_algorithmcs(list_action_function=listarAcoes, execute_action_function=executarAcao, hash_function=funcaoHash, cmp_function=cmpEstados)
    
    solution = busca.BFS(E0, Eobj)
    solution.E0 = decoding(solution.E0)
    solution.Ef = decoding(solution.Ef)
    solution.states = [decoding(x) for x in solution.states]
    
    return solution.states

def DFS_Iter_solution(E0):

    busca = DFSIterative.DFS_algorithmcs(list_action_function=listarAcoes, execute_action_function=executarAcao, hash_function=funcaoHash, cmp_function=cmpEstados)
    
    solution = busca.DFS(E0, Eobj, 18)
    solution.E0 = decoding(solution.E0)
    solution.Ef = decoding(solution.Ef)
    solution.states = [decoding(x) for x in solution.states]
    
    return solution.states

def DFS_Recr_solution(E0):

    busca = DFSRecursive.DFS_algorithmcs(list_action_function=listarAcoes, execute_action_function=executarAcao, hash_function=funcaoHash, cmp_function=cmpEstados)
    
    solution = busca.DFS(E0, Eobj, 18)
    solution.E0 = decoding(solution.E0)
    solution.Ef = decoding(solution.Ef)
    solution.states = [decoding(x) for x in solution.states]
    
    return solution.states

#parser = argparse.ArgumentParser()
#parser.add_argument("-o", nargs="?", type=int, help="O formato do quebra-cabeça. Default = 3. Ex: 3, 4,... ")
#parser.add_argument("-m", nargs="?", type=str, help="Algoritmo de busca. Default = BFS. Ex: BFS ou DFSI ou DFSR")
#parser.add_argument("-E0", nargs="?", type=str, help="Estado inicio. Default/Ex: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]\n")
#parser.add_argument("-Ef", nargs="?", type=str, help="Estado fim. Default/Ex: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]\n")
#
#sysargs = sys.argv[1:]
#if len(sysargs) == 0:
#    sysargs = ["-h"]
#
#
#args = vars(parser.parse_args(sysargs))
#print(args)
