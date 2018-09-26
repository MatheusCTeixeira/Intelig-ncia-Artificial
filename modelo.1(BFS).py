
import BFS

#--Estado inicial
E0 =  "S"

#--Estado final
Eobj = "R"


Movimentos = {"S":["B", "C"],\
              "B":["D", "E"],\
              "C":["H", "I"],\
              "D":["J", "L"],\
              "E":["L", "M"],\
              "H":["M", "N"],\
              "I":["N", "O"],\
              "L":["P"     ],\
              "M":["P", "Q"],\
              "N":["Q"     ],\
              "P":["R"     ],\
              "Q":["R"     ],\
              "R":[        ],\
              "J":[        ],\
              "O":[        ]

}

#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    #Todos os movimentos possíveis a partir deste nó
    acoesPossiveis = Movimentos[Et]

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
     
    return Ea == Eb
#------------------------------------------------

def funcaoHash(Ea):
    return int(ord(Ea)) % 30

busca = BFS.BFS_algorithmcs(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)


for step in busca.BFS(E0, Eobj):
    print("mover-se para " + str(step.action) + ", ", end=' ') 