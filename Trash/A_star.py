import Graph
import Node
import math
from collections import deque


def min_edge(edge, heuristic):
    minv = heuristic(edge[0].state)
    pos = 0
    
    for node in edge:
        val = heuristic(node.state)
        if (val < minv):
            pos = pos + 1        
            minv = val

    return pos 

class A_star_algorthmcs:
    def __init__(self, list_action_function, execute_action_function,\
                       hash_function, cmp_function, heuristic):
        self.list_action_function = list_action_function
        self.execute_action_function = execute_action_function
        self.hash_function = hash_function
        self.cmp_function = cmp_function
        self.heuristic = heuristic


    def trace_solution(self, state_objective):
        solution = []
        for node in self.graph.graphs[len(self.graph.graphs) - 1]:
            if self.cmp_function(node.state, state_objective) == True:                
                solution.append(node)
        
        if len(solution) > 0:
            while (solution[0].parent != None):
                solution.insert(0, solution[0].parent)

        return solution



    def A_star(self, state_origin, state_objective):
        self.graph = Graph.graph(self.hash_function, self.cmp_function)
        edge = [Node.node(state_origin, "#")]

        solution_found = self.cmp_function(state_origin, state_objective)

        while (len(edge) > 0 and solution_found == False):
            key = min_edge(edge, self.heuristic)
            currentNode = edge.pop(key)
            
            actions = self.list_action_function(currentNode.state)

            for action in actions:
                # Create a new state from currentNode.state + action
                state = self.execute_action_function(currentNode.state, action)
                
                # Create a new node from state
                new_node = Node.node(state, action, currentNode)

                # Add the node to graph
                is_new_state = self.graph.append(new_node)

                # Add the node to edge
                if (is_new_state == True):
                    edge.append(new_node)

                solution_found = solution_found or self.cmp_function(state, state_objective)
                
        
        return self.trace_solution(state_objective)
