from queue import PriorityQueue 
from .Algorthims import Algorithim

class AS(Algorithim):
    """A-Star Search (A*)"""
    def __init__(self, current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name, file_name, graph) 

    def search(self):
        queue = PriorityQueue()  
        visited = set()  

        parent = {self.current_node: None} 
        path_cost = {self.current_node: 0}  

        queue.put((self.heuristic(self.graph, self.current_node, self.goal_node), self.current_node))

        while not queue.empty():
            _, node = queue.get() 
            if node in visited: 
                continue

            visited.add(node) 
            self.current_node = node

            if node in self.goal_node:
                self.found = True
                break

            for neighbor in self.graph.return_edges(node).keys():
                neighbor = int(neighbor) 

                if neighbor in visited: 
                    continue

                new_cost = path_cost[node] + self.graph.return_edges(node)[neighbor]

                if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                    path_cost[neighbor] = new_cost 
                    parent[neighbor] = node 

                    priority = new_cost + self.heuristic(self.graph, neighbor, self.goal_node)

                    queue.put((priority, neighbor))
                    self.nodes_created += 1

        if self.found:
            self.path = self.reconstruct_path(parent)
        else:
            print("no path found")
            self.path = []

        self.result()

    def reconstruct_path(self, parent): 
        path = [] 
        node = self.current_node 

        while node is not None: 
            path.append(node) 
            node = parent.get(node) 

        return path[::-1]
    
        #Manhattan Distance
    def heuristic(self, graph, node, goals): 
        if not goals:
            return 0

        x1, y1 = graph.nodes[int(node)]
        distances = []

        for goal in goals:
            x2, y2 = graph.nodes[int(goal)]
            dist = abs(x1 - x2) + abs(y1 - y2)
            distances.append(dist)

        return min(distances)
