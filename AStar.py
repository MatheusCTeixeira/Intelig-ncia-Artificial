
import Node
import Graph
import bisect
import solution



# It's class implement A* Algorithmics
class A_Star:
    # @list_action_function: this function list all possible states from a state
    # @execute_action_function: this function execute a action, returned by list_action_function, in a state
    # @hash_function: this function simplify the search
    # @cmp_function: this function compare two states and determine if they are equals
    def __init__(self, list_action_function, execute_action_function,\
                       hash_function, cmp_function, heuristic_function):
        self.list_action_function = list_action_function
        self.execute_action_function = execute_action_function
        self.hash_function = hash_function
        self.cmp_function = cmp_function
        self.heuristic_function = heuristic_function
        self.id = 1
    
    def get_id(self): 
        self.id = self.id + 1       
        return self.id

    #@It's function execute the algorithmic and return the solution, if any
    #@initial_state: It's expected a state of form [State, Cost, Heuristic]
    #@objective_state: It's have the same form of the above param and represent the objective, ie, the final state
    def A_Star(self, initial_state, objective_state):
        self.graph = Graph.graph(self.hash_function, self.cmp_function, \
                        lambda new_node, old_node: new_node.cost_heuristic > old_node.cost_heuristic)        

        first_node = Node.node(initial_state, " ") #f is the sum of cost and heuristic
        first_node.cost_heuristic = 0
        
        self.graph.append(first_node)
        edge = [first_node]    
        edge_index = [first_node.cost_heuristic]    

        solution = False
        while len(edge) > 0:

            f, current_node = edge_index.pop(0), edge.pop(0)           
            
            if self.cmp_function(current_node.state[0], objective_state[0]) == True:
                solution = current_node
                break

            actions = self.list_action_function(current_node.state[0])

            
            for action in actions:
                new_state = self.execute_action_function(current_node.state[0], action)
                new_node = Node.node(new_state, action, current_node)
                new_node.cost_heuristic = current_node.cost_heuristic + 1  #Attach f to node 

                heuristic_value = self.heuristic_function(new_state[0], objective_state[0])
                
                is_new_state = self.graph.append(new_node)

                if (is_new_state == True):                        
                    cost_more_heurist = new_node.cost_heuristic + heuristic_value                
                    inserted_at_index = bisect.bisect(edge_index, cost_more_heurist)      
                    edge_index.insert(inserted_at_index, cost_more_heurist) 
                    edge.insert(inserted_at_index, new_node)
                    
        self.graph.status()
        return self.trace_solution(initial_state, objective_state, solution)
        
    #   It's function trace the solution from node parent's and return a list with 
    #   all nodes from initial state to objective state, if there is a solution
    #
    # @node: This parameter is the node where the state is the objective    
    def trace_solution(self, E0, Ef, node_solution):
        actions = []
        states = []

        if E0 == Ef:
            actions.append(" ")
            states.append(E0)           
        else:
            temp = node_solution
            while temp != None:
                states.insert(0, temp.state)
                actions.insert(0, temp.action)
                temp = temp.parent

        return solution.solution(E0, Ef, actions, states)

            




        