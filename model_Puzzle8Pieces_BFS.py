
#from PIL import Image, ImageDraw
import BFS
import math
import time

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
#E0 =  encoding( [ [0,2,3] ,  [4,5,6] , [7,8, 1]])
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

#busca = BFS.BFS_algorthmcs(listarAcoes, executarAcao, funcaoHash, cmpEstados)
start_time = time.time()

busca = BFS.BFS_algorithmcs(listarAcoes, executarAcao, funcaoHash, cmpEstados)
vec = [ str(x.action) for x in busca.BFS(E0, Eobj)]

for v in vec:
    print(v)

print("---- %s seconds ----" %(time.time() - start_time))