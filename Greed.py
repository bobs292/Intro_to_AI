from Algorthims import Algorithim
import math

class Greed(Algorithim):

    def __init__(self, current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name, file_name, graph)

    def search(self):
        costs = {}
        visited = []
        path = []
        while not self.found:
            path.append(self.current_node)
            visited.append(self.current_node)
            if self.current_node == self.goal_node:
                self.found = True
                break
            costs.clear()
            for neighbor in self.graph.return_edges(self.current_node):
                neighbor = int(neighbor)
                if neighbor in visited:
                    continue
                costs[neighbor] = self.total_cost_to_goal(neighbor)
            best_cost = float('inf')
            best_node = None
            for node in costs:
                if costs[node] < best_cost:
                    best_cost = costs[node]
                    best_node = node
            if best_node is None:
                break
            self.current_node = best_node
        self.path = path
        self.result()


    def total_cost_to_goal(self, node):
        x2, y2 = (self.graph.nodes[node])
        min_cost = float('inf')
        goals = self.goal_node if isinstance(self.goal_node, list) else [self.goal_node]
        for goal in goals:
            goal = int(goal)
            x1, y1 = (self.graph.nodes[goal])
            ans = math.dist((x2,y2),(x1,y1))
            if ans < min_cost:
                min_cost = ans
        return min_cost
