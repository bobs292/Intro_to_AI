from .Graph import Graph

class Algorithim:
    def __init__(self, current_node, goal_node, name, file_name, graph):
        self.name = name
        self.found = False
        self.path = []
        self.current_node = current_node
        self.goal_node = goal_node
        self.graph = graph
        self.file_name = file_name
    
    def verify_node(self, node):
        if node in self.goal_node:
            self.result()
            self.found = True
    
    def result(self):
        print(self.file_name, self.name)
        print("Goal/s: " + str(self.goal_node), "Path Length: " + str(len(self.path)))
        print("Path: " + str(self.path))

