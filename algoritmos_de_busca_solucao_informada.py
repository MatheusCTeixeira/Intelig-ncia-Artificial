import AStar

from modelo_quebra_cabeca_Astar import listarAcoes
from modelo_quebra_cabeca_Astar import executarAcao
from modelo_quebra_cabeca_Astar import funcao_hash
from modelo_quebra_cabeca_Astar import comparar_estados
from modelo_quebra_cabeca_Astar import encoding
from modelo_quebra_cabeca_Astar import decoding
from modelo_quebra_cabeca_Astar import heuristica_peca_fora_do_lugar
from modelo_quebra_cabeca_Astar import heuristica_distancia_de_manhattan

import modelo_quebra_cabeca_Astar

from time import time

#   A* com heuristica "peças fora do lugar"
def AStar_H1_solution(estado_inicial, estado_objetivo):

    time_init = time()
    busca = AStar.A_Star(   list_action_function=listarAcoes, execute_action_function=executarAcao, \
                        hash_function = funcao_hash, cmp_function = comparar_estados,\
                        heuristic_function=heuristica_peca_fora_do_lugar)

    N = len(estado_inicial)
    estado_inicial = [encoding(estado_inicial), 0]
    estado_objetivo = [encoding(estado_objetivo), 0]

    solution = busca.A_Star(estado_inicial, estado_objetivo)
    solution.E0 = decoding(estado_inicial[0])
    solution.Ef = decoding(estado_objetivo[0])
    solution.states = [decoding(x[0]) for x in solution.states]
    solution.duration = time() - time_init
    solution.deepth = busca.graph.branching_factor()
    solution.width = busca.graph.deepth_factor()

    return solution

#   A* com heuristica "distancia de manhattan"
def AStar_H2_solution(estado_inicial, estado_objetivo):

    time_init = time()
    busca = AStar.A_Star(   list_action_function=listarAcoes, execute_action_function=executarAcao, \
                        hash_function = funcao_hash, cmp_function = comparar_estados,\
                        heuristic_function=heuristica_distancia_de_manhattan)

    N = len(estado_inicial)
    estado_inicial = [encoding(estado_inicial), 0]
    estado_objetivo = [encoding(estado_objetivo), 0]

    solution = busca.A_Star(estado_inicial, estado_objetivo)
    solution.E0 = decoding(estado_inicial[0])
    solution.Ef = decoding(estado_objetivo[0])
    solution.states = [decoding(x[0]) for x in solution.states]
    solution.duration = time() - time_init
    solution.deepth = busca.graph.branching_factor()
    solution.width = busca.graph.deepth_factor()

    return solution

#res = AStar_H1_solution(modelo_quebra_cabeca_Astar.E0, modelo_quebra_cabeca_Astar.Eobj)
#print(res.actions)