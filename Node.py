

class node:   
    #Node level: depth of hierarchy level
    #Node state: describe the state represented by this node
    #Node action: describe the action applied to the parent of this node to reach this node
    #Node parent: parent
    #Node childrens: childrens
    nID = 0

    def __init__(self, state, action, parent = None):
        self.ID = "NodeID" + str(node.nID) 
        node.nID = node.nID + 1
        
        self.state = state
        self.action = action
        self.parent = parent
        self.childrens = []
        self.cost = 0
        self.heurist = 0
        self.cost_heuristic = 0
        
        if (parent != None):
            self.level = parent.level + 1
            self.parent.childrens.append(self)
        else:
            self.level = 0

    def status(self):
        print("@ID: "         + str(self.ID)             + "\n" + \
              "@level: "      + str(self.level)          + "\n" + \
              "@state: "      + str(self.state)          + "\n" + \
              "@action: "     + str(self.action)         + "\n" + \
              "@childrens: #" + str(len(self.childrens)) + "\n" )
              