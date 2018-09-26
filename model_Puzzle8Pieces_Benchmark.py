
#from PIL import Image, ImageDraw
import DFSIterative
import DFSRecursive
import BFS

import math
import time
import random
import copy

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
E0 =  encoding( [ [3,4,5] , [7,1,0] , [2,8,6]])

#--Estado final
Eobj = encoding([ [1,2,3] ,  [4,5,6] , [7,8, 0]])

#-- Procura a posição atual
def posicaoAtual(Et):       
    mask = 0b1111
    for i in range(0, 9):
        if (Et >> (i * 4)) & mask == 0:      
            return (2 - math.floor(i  / 3), 2 - (i  % 3))
        
#------------------------------------------------


#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    acoesPossiveis = []

    posicao = posicaoAtual(Et)
    
    lin, col = posicao
   
    if (lin > 0):
        acoesPossiveis.append("up")

    if (lin < 2):
        acoesPossiveis.append("down")

    if (col > 0): 
        acoesPossiveis.append("left")

    if (col < 2): 
        acoesPossiveis.append("right")

    return acoesPossiveis
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


steps = 23
E0 = randomize_initial_state(Eobj, steps)
#E0 = encoding([[2, 5, 6], [3, 0, 7], [1, 4, 8]])

print("-------------------------------------------------------------------------\n\n")

busca1 = DFSIterative.DFS_algorithmcs(listarAcoes, executarAcao, funcaoHash, cmpEstados)
busca2 = DFSRecursive.DFS_algorithmcs(listarAcoes, executarAcao, funcaoHash, cmpEstados)
busca3 = BFS.BFS_algorithmcs(listarAcoes, executarAcao, funcaoHash, cmpEstados)

start_time1 = time.time()
vec = [ x for x in busca1.DFS(E0, Eobj, steps)]
print(vec)
print("-----------------------DFS Iter %s seconds -----------------------\n\n" %(time.time() - start_time1))

start_time2 = time.time()
vec = [ x for x in busca2.DFS(E0, Eobj, steps)]
print(vec)
print("-----------------------DFS Recr %s seconds -----------------------\n\n" %(time.time() - start_time2))

start_time3 = time.time()
vec = [ x.action for x in busca3.BFS(E0, Eobj)]
print(vec)
print("-----------------------BFS      %s seconds -----------------------\n\n" %(time.time() - start_time3))

