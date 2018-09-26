
from PIL import Image, ImageDraw
import copy
import busca

#--Estado inicial
E0 =  ("A", 0)

#--Estado final
Eobj = ("J", None)


Movimentos = {"S":[("B", 1) , ("C", 3)],\
              "B":[("C", 1) , ("D", 4)],\
              "C":[("D", 2) , ("E", 2)],\
              "D":[("E", 4) , ("G", 3)],\
              "E":[("G", 1)           ],\
              "G":[                   ]\
}

#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    #Todos os movimentos possíveis a partir deste nó
    acoesPossiveis = Movimentos[Et[0]]

    return acoesPossiveis
#------------------------------------------------

#--Executar ações
def executarAcao( Et, acao):
    #Custo acumulado
    custo = acao[1] + Et[1]
    estado = acao[0]

    return (estado, custo)
           
#------------------------------------------------

#--Compara igualdade de estados
# **** É possivel associar um inteiro a cada estado e
# **** assim a comparação seria direta
def estadosIguais(Ea, Eb):
     
    return Ea[0] == Eb[0]
#------------------------------------------------

# Desenha o estado
def desenharEstado(E, imagem, xy, wh):
    dr = ImageDraw.Draw(imagem)

    # Parâmetros para o desenho
    x,y = xy
    w, h = wh
    dx, dy = w/3, h/3

    # Desenha elemento a elemento do estado E
    for lin in E:
        for value in lin:
            dr.text((x + dx/2, y + dy/2), str(value), fill=(0, 0, 255))
            dr.rectangle((x, y, x + dx, y + dy), outline=(0, 0, 0))
            x = x + dx

        x = xy[0]
        y = y + dy

        
#-----------------------------------------------

#Necessário para utilizar os algorimos de busca
busca.funcLstAction = listarAcoes
busca.funcExeAction = executarAcao
busca.funcCmpState  = estadosIguais

busca.busca(("S", 0), ("G", None), "largura")
print("BFS:")
print(busca.solucao())
print("\n\n\n")
busca.busca(("S", 0), ("G", None), "profundidade")
print("DFS:")
print(busca.solucao())
print("\n\n\n\n")
busca.busca(("S", 0), ("G", None), "custo")
print("UCS:")
print(busca.solucao())