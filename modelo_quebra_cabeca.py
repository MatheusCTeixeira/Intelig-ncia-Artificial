
import DFSIterative
import DFSRecursive
import BFS

from math import log2
from math import ceil

import time
import random
import copy

import argparse

import sys
import math


def find_order(value):
    def calc_bit_length(N): return N ** 2 * ceil(log2(N ** 2))
    value_bit_length = ceil(log2(value))
    N = 1
    diff = value_bit_length - calc_bit_length(N)

    while diff > 7:
        N += 1
        diff = value_bit_length - calc_bit_length(N)

    return N


def encoding(estado_inicial):
    N = len(estado_inicial)
    mask_bitsize = math.ceil(math.log2(N**2))
    mask = 2 ** mask_bitsize - 1
    value = 0

    for line in estado_inicial:
        for v in line:
            value = value << mask_bitsize
            value = value | (mask & v)

    return value


def decoding(value):
    N = find_order(value)
    vl = value
    mask_bitsize = math.ceil(math.log2(N**2))
    mask = 2 ** mask_bitsize - 1
    estado = []
    for j in range(0, N):
        estado.insert(0, [])
        for i in range(0, N):
            estado[0].insert(0, (mask & vl))
            vl = vl >> mask_bitsize

    return estado


# --Estado inicial
#E0 = [[1, 2, 3, 4, 9], [5, 6, 7, 8, 14], [10, 11, 12, 13, 0], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
#E0 = [[1, 2, 3, 7], [4, 5, 6, 11], [8, 9, 10, 0], [12, 13, 14, 15]]
#E0 = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]


# -- Procura a posição atual
def posicaoAtual(estado):
    N = find_order(estado)
    mask_bitsize = ceil(log2(N**2))
    mask = 2 ** mask_bitsize - 1
    for i in range(0, N ** 2):
        if (estado >> (i * mask_bitsize)) & mask == 0:
            return ((N - 1) - math.floor(i / N), (N - 1) - (i % N))

# ------------------------------------------------


# --Lista todos as possiveis ações para determinado estado
def listarAcoes(estado):
    N = find_order(estado)

    acoes_possiveis = []

    posicao = posicaoAtual(estado)

    lin, col = posicao

    if lin > 0:
        acoes_possiveis.append("up")

    if lin < N - 1:
        acoes_possiveis.append("down")

    if col > 0:
        acoes_possiveis.append("left")

    if col < N - 1:
        acoes_possiveis.append("right")

    return acoes_possiveis
# ------------------------------------------------


# --Troca duas posições
def trocaPosicao(estado, p0, p1):
    Etemp = decoding(estado)

    l0, c0 = p0
    l1, c1 = p1

    # swap
    Etemp[l0][c0], Etemp[l1][c1] = Etemp[l1][c1], Etemp[l0][c0]

    return encoding(Etemp)

# ------------------------------------------------


# --Executar ações
def executarAcao(estado, acao):
    posAt = posicaoAtual(estado)
    lin, col = posAt

    if (acao == "up"):
        lin = lin - 1
    elif (acao == "down"):
        lin = lin + 1
    elif (acao == "left"):
        col = col - 1
    elif (acao == "right"):
        col = col + 1

    Et = trocaPosicao(estado, posAt, (lin, col))

    return Et

# ------------------------------------------------

# --Compara igualdade de estados
# **** É possivel associar um inteiro a cada estado e
# **** assim a comparação seria direta


def comparar_estados(Ea, Eb):
    return Ea == Eb
# ------------------------------------------------


def funcao_hash(Et):
    return Et % 50

# ------------------------------------------------


def randomize_initial_state(state_objective, step):

    solution = []
    initial_state = state_objective
    states_already_visited = [state_objective]

    while len(solution) < step:
        # List all possible actions
        acoes = listarAcoes(initial_state)

        # Choice a possibility randolly from the possible actions
        action = acoes[random.randint(0, len(acoes) - 1)]

        temp_state = executarAcao(initial_state, action)

        # Add the step if the state is new
        if states_already_visited.count(temp_state) == 0:
            solution.append(action)
            initial_state = temp_state
            states_already_visited.append(temp_state)

    print("initial state: %s" % str(decoding(initial_state)))
    print("solution: %s" % str(solution))
    return initial_state