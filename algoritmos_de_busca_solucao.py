import BFS
import DFSIterative
import DFSRecursive

from modelo_quebra_cabeca import listarAcoes
from modelo_quebra_cabeca import executarAcao
from modelo_quebra_cabeca import funcao_hash
from modelo_quebra_cabeca import comparar_estados
from modelo_quebra_cabeca import encoding
from modelo_quebra_cabeca import decoding

def BFS_solution(estado_inicial):

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

    return solution.states


def DFS_Iter_solution(estado_inicial):

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

    return solution.states


def DFS_Recr_solution(estado_inicial):

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
    

    return solution.states
