
import DFSRecursive

#--Estado inicial
E0 =  "A"

#--Estadofinal
Eobj = "P"


Movimentos = {"A":["B", "I", "C"],\
              "B":["D", "E"],\
              "C":["F", "G"],\
              "D":["H", "I"],\
              "E":["J", "K"],\
              "F":["L", "M"],\
              "G":["N", "O"],\
              "H":[        ],\
              "I":["P"     ],\
              "J":[        ],\
              "K":[        ],\
              "L":[        ],\
              "M":[        ],\
              "N":[        ],\
              "O":[        ],\
              "P":[        ]

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

busca = DFSRecursive.DFS_algorithmcs(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)


for step in busca.DFS(E0, Eobj, 3):
    print("mover-se para " + str(step) + ", ", end=' ') 
print("")
