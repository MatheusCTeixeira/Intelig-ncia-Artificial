
from math import sqrt

from PIL import ImageDraw
from PIL import Image

from node import Node


      

#List the number of moves possible in this pos
def possible_moves(map, pos):
    possibilities = []
    i, j = pos #9,1
    
    if (j > 0 and map[i][j - 1] == 1):
        possibilities.append((i, j - 1))

    if (j < len(map[i]) - 1 and map[i][j + 1] == 1):
        possibilities.append((i, j + 1))

    if (i > 0 and map[i - 1][j] == 1):
        possibilities.append((i - 1, j))

    if (i < len(map) - 1 and map[i + 1][j] == 1):
       possibilities.append((i + 1, j))

    return possibilities
    
#Remove os nós redundantes, isto é, os nós que possuem apenas um filho/ramo
def remove_redundant_nodes(node):
    temp_node = node.parent

    while len(temp_node.childrens) == 1 and temp_node.parent != None:
        temp_node.parent.childrens.remove(temp_node)
        temp_node.parent.childrens.append(node)
        node.parent = temp_node.parent
        node.cost += 1
        del temp_node

        temp_node = node.parent

#Desfaz as modificações feitas no mapa durante a busca por nós
def reset_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 2:
                map[i][j] = 1

#Identifica os pontos no mapa que impactam nas decisões, isto é, nós com 0 ou mais de uma bifurcação (com execeção do caminho já percorrido) 
def find_nodes(map, start, end):
    first_node = Node(start)
    stack = [first_node]
    nodes = [first_node]

    while len(stack) > 0:
        current_node = stack.pop()
        i, j = current_node.id

        #define o estado como visitado
        map[i][j] = 2

        #Percorre o mapa
        moves = possible_moves(map, (i, j))
        for move in moves:
            #Adiciona todos os possiveis caminhos na pilha
            new_node = Node(move, current_node)
            stack.append(new_node)

        #Remove os nós redundantes
        if len(moves) != 1:
            if current_node.parent != None:
                remove_redundant_nodes(current_node)
            
            #Apply the manhattan heuristic
            current_node.heuristic = sqrt((i-end[0])**2 + (j-end[1])**2)
            nodes.append(current_node)
            
    reset_map(map)

    return nodes

            
#Destaca os nós no mapa
def highlight_nodes(map, nodes):
    for node in nodes:
        i, j = node.id
        map[i][j] = 2

#Desenha o mapa com o percuso e os nós importantes destacados
def drawMap(map, imagesize):
    img = ImageDraw.Image.new(mode="RGB", size=imagesize)
    imgdr = ImageDraw.ImageDraw(img)

    dx = (imagesize[0] - 15)/len(map[0])
    dy = (imagesize[1] - 15)/len(map) 

    colors = [(0, 0, 0), (0, 80, 80), (0, 255, 0)]
    for i in range(len(map)):
        for j in range(len(map[i])):
            color = colors[map[i][j]]
            imgdr.rectangle([j*dx, i*dy, (j+1)*dx, (i+1)*dy], fill=color, outline=(255, 0, 0))
            del color

    img.save("test.png")

#A partir dos nós for os gráfos nos seguinte formato: (ID, Custo, Custo da heurística) 
def nodes_to_dictionary(nodes):
    map = {}
    
    letter = 'A'
    for node in nodes:
        #print(str(node.id) + " is " + letter)
        node.id = letter
        map.update({letter: []})
        letter = chr(ord(letter) + 1)

    for node in nodes:
        for subnode in node.childrens:
            map[node.id].append([subnode.id, subnode.cost, subnode.heuristic])

    return map
    

