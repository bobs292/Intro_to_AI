from .Algorthims import Algorithim

class Beam(Algorithim):
    def __init__(self, current_node, goal_node, name, file_name, graph, beam_width=3):
        super().__init__(current_node, goal_node, name, file_name, graph)
        self.beam_width = beam_width

    def search(self):
        beam = [[self.current_node]]

        while beam:
            next_candidates = []

            for path in beam:
                node = path[-1]

                if node in self.goal_node:
                    self.path = path
                    self.found = True
                    self.result()
                    return

                neighbours = sorted(self.graph.return_edges(node).keys())

                for neighbour in neighbours:
                    if neighbour not in path:
                        next_candidates.append(path + [neighbour])
                        self.nodes_created += 1

            if not next_candidates:
                break

            next_candidates.sort(key=lambda p: self.heuristic(p[-1]))
            beam = next_candidates[:self.beam_width]

        if not self.found:
            print("No path found")
            self.path = []
            return

        self.result()

    
    def heuristic(self, node):
        x1, y1 = self.graph.nodes[int(node)]
        
        closest_distance = float('inf')

        for goal in self.goal_node:
            x2, y2 = self.graph.nodes[int(goal)]
            
            distance = abs(x1 - x2) + abs(y1 - y2)
            
            if distance < closest_distance:
                closest_distance = distance

        return closest_distance