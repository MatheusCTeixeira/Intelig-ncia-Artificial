
from enum import Enum

import Graph
import Node
import copy

class Result(Enum):
    SUCCESS = 1
    FAIL    = 2
    FALSE   = 3

class DFS_algorithmcs:
    def __init__(self, list_action_function, execute_action_function,\
                       hash_function, cmp_function):
        self.list_action_function = list_action_function
        self.execute_action_function = execute_action_function
        self.hash_function = hash_function
        self.cmp_function = cmp_function

    #--------------------------------------------------------------------------

    def DFS_recursive(self, node, state_objective, lvl, graph):   
        #Test solution
        if (self.cmp_function(node.state, state_objective) == True):            
            return node

        if (lvl == 0):
            return Result.FAIL

        #List possibles actions
        actions = self.list_action_function(node.state)

        if (len(actions) == 0):
            return Result.FAIL
      
        for action in actions:
           
            #Create a new state
            new_state = self.execute_action_function(node.state, action)
            
            #Create a new node
            new_node = Node.node(new_state, action, node)
            
            #Return if the node is new or not in the graph
            is_new_state = graph.append(new_node)

            if (is_new_state == True):                                   
                result = self.DFS_recursive(new_node, state_objective, lvl - 1, graph)
                if result != Result.FAIL:
                    return result
                    
        return Result.FAIL

    #--------------------------------------------------------------------------

    def DFS(self, state_origin, state_objective, lvl):
        #Create the graph
        #Prefer the node with lowest level
        graph = Graph.graph(self.hash_function, self.cmp_function, \
                            lambda new_node, old_node: new_node.level < old_node.level)
        

        first_node = Node.node(state_origin, "$")
        graph.append(first_node)

        result = self.DFS_recursive(first_node, state_objective, lvl, graph)
        
        if result != Result.FAIL:
            return self.trace_solution(result)
        else:
            return []

    #--------------------------------------------------------------------------

    def trace_solution(self, node):
        solution = []
        temp_node = node

        while (temp_node != None):
            solution.insert(0, temp_node.action)
            temp_node = temp_node.parent

        return solution

    #--------------------------------------------------------------------------