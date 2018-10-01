
import AStar

#--Estado inicial
E0 =  ["A", 0, 0]

#--Estadofinal
Eobj = ["J", 0, 0]


Movimentos = {"A":[["B", 3, 3], ["C", 2, 2]],\
              "B":[["D", 4, 4], ["E", 3, 3]],\
              "C":[["F", 1, 1], ["G", 2, 2]],\
              "D":[["H", 5, 5]             ],\
              "E":[["H", 2, 2], ["J", 3, 3]],\
              "F":[["J", 10, 1], ["I", 2, 2]],\
              "G":[["I", 1, 1]             ],\
              "H":[["J", 1, 1]             ],\
              "I":[["J", 3, 3]             ],\
              "J":[                        ]        
}

#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    #Todos os movimentos possíveis a partir deste nó
    acoesPossiveis = Movimentos[Et[0]]

    return acoesPossiveis
#------------------------------------------------

#--Executar ações
def executarAcao( Et, acao):

    return acao
           
#------------------------------------------------

#--Compara igualdade de estados
# **** É possivel associar um inteiro a cada estado e
# **** assim a comparação seria direta
def cmpEstados(Ea, Eb):
     
    return Ea[0] == Eb[0]
#------------------------------------------------

def funcaoHash(Ea):
    return int(ord(Ea[0])) % 30

busca = AStar.A_Star(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)


for step in busca.A_Star(E0, Eobj):
    print(str(step) + ", ", end=' ') 
print("")
