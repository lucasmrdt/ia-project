from interfaces import IAlgorithm, IInstance, IAction, IHeuristic, IState, ISolution 
import math

class HeuristiqueMST(TCPHeuristic):
   def get_h(self, state: TCPState, instance: TCPInstance) -> int:
        visited_nodes = state.visited_nodes
        unvisited_nodes = state.unvisited_nodes
        
        h_val = 0

        for vis_node in visited_nodes:
            min_weigh = math.inf
            new_vis_node = None
            for unvis_node in unvisited_nodes:
                if vis_node in self.instance.adj_mat and unvis_node in self.instance.adj_mat[vis_node]:
                    if self.instance.adj_mat[vis_node][unvis_node] < min_weigh:
                        min_weigh = self.instance.adj_mat[vis_node][unvis_node]
                        new_vis_node = unvis_node
            h+=min_weigh
            visited_nodes.append(unvis_node)
            unvisited_nodes.remove(unvis_node)
        
        return h_val 