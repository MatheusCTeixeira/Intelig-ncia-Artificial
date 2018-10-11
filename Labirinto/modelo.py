
import AStar
import DFSIterative
import BFS
import labirinto

import time

map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
       [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0], \
       [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0], \
       [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0], \
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], \
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0], \
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0], \
       [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], \
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1], \
       [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
       [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], \
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0], \
       [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], \
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]    



#--Estado inicial
E0 =  ("A", 0, 0)

#--Estado final
Eobj = ("P", 0, 0)

#--Transforma o labirinto em nós
nodes = labirinto.find_nodes(map, (9,0), (8, 20))

labirinto.highlight_nodes(map, nodes)
labirinto.drawMap(map, (700, 500))

#--Transforma os nós em uma tabela
Movimentos = labirinto.nodes_to_dictionary(nodes)

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


busca1 = BFS.BFS_algorithmics(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)


busca2 = DFSIterative.DFS_algorithmcs(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)

busca3 = AStar.A_Star_algorithmics(list_action_function=listarAcoes, execute_action_function=executarAcao, \
                           hash_function = funcaoHash, cmp_function = cmpEstados)


#print("Algoritmo: BFS")
#print("Borda/Iteração:")
#solution = busca1.BFS(E0, Eobj)
#print("Solução:")
#start_time = time.time()
#for step in solution:
#    print("mover-se para " + str(step.action) + ", ", end=' ') 
#print("\nduration: %sseg" %(time.time() - start_time) )
#
#
#print("\n-------------------------------------------------------------------\n")
#
#
#print("\n\nAlgoritmo: DFS")
#print("Borda/Iteração:")
#solution = busca2.DFS(E0, Eobj, 15)
#print("Solução:")
#start_time = time.time()
#for step in solution:
#    print("mover-se para " + str(step) + ", ", end=' ') 
#print("\nduration: %sseg" %(time.time() - start_time) )
#print("\n-------------------------------------------------------------------\n")

print("Algoritmo: A Star")
print("Borda/Iteração:")
solution = busca3.A_Star(E0, Eobj)
print("Solução:")
start_time = time.time()
for step in solution:
    print("mover-se para " + str(step) + ", ", end=' ') 
print("\nduration: %sseg" %(time.time() - start_time) )




print("\n-------------------------------------------------------------------\n")