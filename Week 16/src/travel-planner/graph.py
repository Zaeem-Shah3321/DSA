class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.weights = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes.add(value)
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)  
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight  