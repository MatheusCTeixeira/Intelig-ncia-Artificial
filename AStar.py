
import Node
import Graph
import bisect



# It's class implement A* Algorithmics
class A_Star:
    # @list_action_function: this function list all possible states from a state
    # @execute_action_function: this function execute a action, returned by list_action_function, in a state
    # @hash_function: this function simplify the search
    # @cmp_function: this function compare two states and determine if they are equals
    def __init__(self, list_action_function, execute_action_function,\
                       hash_function, cmp_function):
        self.list_action_function = list_action_function
        self.execute_action_function = execute_action_function
        self.hash_function = hash_function
        self.cmp_function = cmp_function
        self.id = 1
    
    def get_id(self): 
        self.id = self.id + 1       
        return self.id

    #@It's function execute the algorithmic and return the solution, if any
    #@initial_state: It's expected a state of form (State, Cost, Heuristic)
    #@objective_state: It's have the same form of the above param and represent the objective, ie, the final state
    def A_Star(self, initial_state, objective_state):
        self.graph = Graph.graph(self.hash_function, self.cmp_function, \
                        lambda new_node, old_node: new_node.cost_heuristic < old_node.cost_heuristic)        

        f, first_node = initial_state[1] + initial_state[2], Node.node(initial_state, "$") #f is the sum of cost and heuristic
        first_node.cost_heuristic = f
        self.graph.append(first_node)
        edge = [(f, first_node)]        

        solution = False
        while len(edge) > 0:
            f, current_node = edge.pop()

            if self.cmp_function(current_node.state[0], objective_state[0]) == True:
                solution = current_node
                break

            actions = self.list_action_function(current_node.state)

            for action in actions:
                new_state = self.execute_action_function(current_node.state, action)
                new_state[1] += current_node.state[1] #Sum the cost
                new_node = Node.node(new_state, action, current_node)
                
                #Attach f to node
                f_new = new_state[1] + new_state[2]
                new_node.cost_heuristic = f_new

                is_new_state = self.graph.append(new_node)

                if (is_new_state == True):
                    edge.append((f_new, new_node))

            edge.sort(key = lambda v: v[0], reverse=True) #Order the edge by the lowest f's first        
        
        return self.trace_solution(solution)
        
    #   It's function trace the solution from node parent's and return a list with 
    #   all nodes from initial state to objective state, if there is a solution
    #
    # @node: This parameter is the node where the state is the objective    
    def trace_solution(self, node):
        solution = []

        if type(node) is not Node.node:
            return solution

        temp_node = node
        while temp_node != None:
            solution.insert(0, temp_node.action)
            temp_node = temp_node.parent

        return solution

            




        