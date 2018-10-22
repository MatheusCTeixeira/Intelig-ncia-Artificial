from math import inf

class solution:
    """ Esta classe serve para padronizar as soluções retornadas pelos algoritmos de busca  """
    
    def __init__(self, E0, Ef, actions, states):
        self.E0 = E0
        self.Ef = Ef
        self.actions = actions
        self.states = states
        self.duration = inf
        self.width = inf
        self.deepth = inf