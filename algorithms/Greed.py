from .Algorthims import Algorithim
import math

class Greed(Algorithim):

    def __init__(self, current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name, file_name, graph)

    def search(self):
        open_list = [self.current_node]
        visited = set()

        #needed for the reverse
        parent = {}
        parent[self.current_node] = None
        print(self.graph.nodes)
        print(self.graph.graph)
        print(self.current_node) 
        print(self.goal_node)
        while open_list:
            best_node = min(open_list, key=self.total_cost_to_goal)
            open_list.remove(best_node)
            if best_node in visited:
                continue
            visited.add(best_node)
            self.current_node = best_node
            if best_node in self.goal_node:
                self.goal_node = best_node
                self.found = True
                break
            for neighbor in self.graph.return_edges(best_node).keys():
                neighbor = int(neighbor)
                if neighbor in visited:
                    continue
                if neighbor not in open_list:
                    open_list.append(neighbor)
                    parent[neighbor] = best_node

        if self.found:

            self.path = self.reconstruct_path(parent)
        else:
            print("no path found")
            self.path = []
        self.result()


    def reconstruct_path(self,parent):
        path = []
        node = self.current_node
        while node is not None:
            path.append(node)
            node = parent.get(node)
        path.reverse()  
        return path


    def total_cost_to_goal(self,node):
        node = int(node)
        x2, y2 = self.graph.nodes[node]
        min_cost = float('inf')
        goals = self.goal_node if isinstance(self.goal_node,list) else [self.goal_node]
        for goal in goals:
            goal = int(goal)    
            x1, y1 = self.graph.nodes[goal]
            cost = math.dist((x2,y2),(x1,y1))
            if cost < min_cost:
                min_cost = cost
        return min_cost