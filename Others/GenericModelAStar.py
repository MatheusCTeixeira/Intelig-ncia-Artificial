
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
#----@Et o estado no qual se quer listar as ações
#----@Retorna uma lista com os estados possiveis
def listarAcoes(Et):
    acoesPossiveis = []

    #Todos os movimentos possíveis a partir deste nó
    for item in Movimentos[Et]:
        acoesPossiveis.append(item[0])

    return acoesPossiveis
#------------------------------------------------

#--Executar ações
#----@Et: o estado atual
#----@acao: a ação a se aplicar
#----@Retorna uma lista na forma [Estado alcançado, custo, heuristica ]
def executarAcao( Et, acao):
    
    for item in Movimentos[Et]:        
        if item[0] == acao:
            return item

    return None
           
#------------------------------------------------

#--Compara igualdade de estados
#----É possivel associar um inteiro a cada estado e
#----assim a comparação seria direta
#----@Ea: estado 1
#----@Eb: estado 2
#----@Retorna True se Ea == Eb e False caso contrário
def cmpEstados(Ea, Eb):
     
    return Ea == Eb
#------------------------------------------------

def funcaoHash(Ea):
    return int(ord(Ea[0])) % 30

busca = AStar.A_Star(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)


for step in busca.A_Star(E0, Eobj):
    print(str(step) + ", ", end=' ') 
print("")
