import BFS
import DFSIterative
import DFSRecursive

from modelo_quebra_cabeca import listarAcoes
from modelo_quebra_cabeca import executarAcao
from modelo_quebra_cabeca import funcao_hash
from modelo_quebra_cabeca import comparar_estados
from modelo_quebra_cabeca import encoding
from modelo_quebra_cabeca import decoding

import modelo_quebra_cabeca_Astar

from time import time

def BFS_solution(estado_inicial):

    time_init = time()
    busca = BFS.BFS_algorithmcs(list_action_function=listarAcoes,
                                execute_action_function=executarAcao,
                                hash_function=funcao_hash,
                                cmp_function=comparar_estados)

    N = len(estado_inicial)
    estado_inicial = encoding(estado_inicial)
    estado_objetivo = encoding([[i*N + j for j in range(N)] for i in range(N)])

    solution = busca.BFS(estado_inicial, estado_objetivo)
    solution.E0 = decoding(estado_inicial)
    solution.Ef = decoding(estado_objetivo)
    solution.states = [decoding(x) for x in solution.states]
    solution.duration = time() - time_init
    solution.deepth = busca.graph.branching_factor()
    solution.width = busca.graph.deepth_factor()

    return solution


def DFS_Iter_solution(estado_inicial):

    time_init = time()
    busca = DFSIterative.DFS_algorithmcs(list_action_function=listarAcoes,
                                         execute_action_function=executarAcao,
                                         hash_function=funcao_hash,
                                         cmp_function=comparar_estados)

    N = len(estado_inicial)
    estado_inicial = encoding(estado_inicial)
    estado_objetivo = encoding([[i*N + j for j in range(N)] for i in range(N)])

    solution = busca.DFS(estado_inicial, estado_objetivo, 18 - 5 * (N - 3))
    
    solution.E0 = decoding(estado_inicial)
    solution.Ef = decoding(estado_objetivo)    
    solution.states = [decoding(x) for x in solution.states]   
    solution.duration = time() - time_init
    solution.deepth = busca.graph.branching_factor()
    solution.width = busca.graph.deepth_factor()


    return solution


def DFS_Recr_solution(estado_inicial):

    time_init = time()
    busca = DFSRecursive.DFS_algorithmcs(list_action_function=listarAcoes,
                                         execute_action_function=executarAcao,
                                         hash_function=funcao_hash,
                                         cmp_function=comparar_estados)

    N = len(estado_inicial)
    estado_inicial = encoding(estado_inicial)
    estado_objetivo = encoding([[i*N + j for j in range(N)] for i in range(N)])

    solution = busca.DFS(estado_inicial, estado_objetivo, 18 - 5 * (N - 3))
    
    solution.E0 = decoding(estado_inicial)
    solution.Ef = decoding(estado_objetivo)    
    solution.states = [decoding(x) for x in solution.states]
    solution.duration = time() - time_init
    solution.deepth = busca.graph.branching_factor()
    solution.width = busca.graph.deepth_factor()    

    return solution

def HC_solution(estado_inicial):

    time_init = time()
    busca = modelo_quebra_cabeca_Astar.AStar.A_Star(\
        list_action_function=modelo_quebra_cabeca_Astar.listarAcoes,\
        execute_action_function=modelo_quebra_cabeca_Astar.executarAcao, \
        hash_function = modelo_quebra_cabeca_Astar.funcao_hash, \
        cmp_function = modelo_quebra_cabeca_Astar.comparar_estados)

    N = len(estado_inicial)
   
    estado_inicial = [modelo_quebra_cabeca_Astar.encoding(estado_inicial), 0, 0]
    estado_objetivo = [[i*N + j for j in range(N)] for i in range(N)]
    estado_objetivo = [modelo_quebra_cabeca_Astar.encoding(estado_objetivo), 0, 0]

    solution = busca.A_Star(estado_inicial, estado_objetivo)
    
    solution.E0 = modelo_quebra_cabeca_Astar.decoding(estado_inicial[0])
    solution.Ef = modelo_quebra_cabeca_Astar.decoding(estado_objetivo[0])    
    solution.states = [modelo_quebra_cabeca_Astar.decoding(x[0]) for x in solution.states]
    solution.duration = time() - time_init
    solution.deepth = busca.graph.branching_factor()
    solution.width = busca.graph.deepth_factor()    

    return solution

#print(HC_solution([ [3,4,5] , [7,1,0] , [2,8,6]]))