from Graph import Graph
class Greed:
    def __init__(self, current_node, goal_node):
        self.path = []
        self.current_node = current_node
        self.goal_node = goal_node
        self.visited = set()
    
    def search(self,graph):
        while self.current_node != self.goal_node:
            self.path.append(self.current_node)
            self.visited.add(self.current_node)
            connect_nodes = graph.graph[self.current_node]

            best_node = None
            best_cost = float('inf')
            
            for node in connect_nodes:
                if node in self.visited:
                    continue
                    
                cost = self.total_cost_to_goal(graph,node)
                
                if cost < best_cost:
                    best_cost = cost
                    best_node = node
                    
            if best_node is None:
                return None
                
            self.current_node = best_node
        self.path.append(self.goal_node)
        return self.path

    def total_cost_to_goal(self, graph, start):
        queue = [(start,0)]
        visited = set()

        while queue:
            node,cost = queue.pop() 

            if node == self.goal_node:
                return cost
            
            if node not in visited:
                visited.add(node)

                for connect_node in graph.graph[node]:
                    edge_cost = graph.graph[node][connect_node]
                    queue.append((connect_node, cost + edge_cost))
                    
        return float('inf')

    
