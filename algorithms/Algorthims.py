from .Graph import Graph

class Algorithim:
    """
    Base class for all search algorithms.

    Attributes:
        name (str): Name of the search algorithm.
        found (bool): Indicates whether a goal node has been found.
        path (list[int]): The final solution path from start node to goal node.
        current_node (int): The current node being processed.
        goal_node (list[int]): List of possible goal nodes.
        graph (Graph): Graph object containing nodes and edges.
        file_name (str): Name of the input file used for the search.
        nodes_created (int): Number of nodes generated during the search.
    """
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
        """
            Prints out the search algorithms stats in the structure:
            File_Name Algorithm_Name
            Goal_Node Nodes_Created
            Path
        
        """
        print(self.file_name, self.name)
        print(str(self.path[-1]), str(self.nodes_created))
        print(str(self.path))