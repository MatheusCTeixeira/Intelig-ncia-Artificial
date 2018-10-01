

class Node:
    id = 0
    def __init__(self, id, parent = None):
        self.childrens = []
        self.parent = parent
        self.id = id
        self.cost = 0
        self.heuristic = 0
        
        if parent != None:
            self.parent.childrens.append(self)
        
        