from .Graph import Graph

class Algorithim:
    def __init__(self, current_node, goal_nodes, name, file_name, graph):
        self.name = name
        self.found = False
        self.path = []
        self.current_node = int(current_node)
        self.goal_node = [int(i) for i in goal_nodes]
        self.graph = graph
        self.file_name = file_name
        self.nodes_created = 1
    
    def verify_node(self, node):
        if node in self.goal_node:
            self.result()
            self.found = True
    
    def result(self):
        print(self.file_name, self.name)
        print(str(self.goal_node[-1]), str(self.nodes_created))
        print(str(self.path))