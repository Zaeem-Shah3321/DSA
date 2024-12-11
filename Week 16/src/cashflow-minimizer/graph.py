class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.balances = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes.add(value)
            self.edges[value] = []
            self.balances[value] = 0

    def add_edge(self, from_node, to_node, amount):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        self.edges[from_node].append((to_node, amount))
        self.balances[from_node] -= amount
        self.balances[to_node] += amount