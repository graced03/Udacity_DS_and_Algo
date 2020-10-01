import math
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self) -> bool:
        return len(self.elements) == 0
    
    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
def find_path_recursive(path, goal):
    if goal == None:
        return []
    final_path = find_path_recursive(path, path[goal])
    return final_path + [goal]

def est_distance(M, first_node, second_node):
    p1 = M.intersections[first_node]
    p2 = M.intersections[second_node]

    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def shortest_path(M, start, goal):
#     print("shortest path called")

    all_nodes = M.intersections.keys()
    h_path = dict()
    # for node in all_nodes:
    #     if node == goal:
    #         h_path.update({node: 0})
    #     else:
    #         h_path.update({node: est_distance(node, goal)})

    g_path = dict()
    for node in all_nodes:
        neighbours = M.roads[node]
        g_path.update({(node, neighbour): est_distance(M, node, neighbour) for neighbour in neighbours})
    
    frontier_nodes = PriorityQueue()
    frontier_nodes.put(start, 0)

    path_cost = {start: 0}
    path = {start: None}

    while not frontier_nodes.empty():

        current_node = frontier_nodes.get()
        if current_node == goal:
            break

        for neighbour in M.roads[current_node]:
#             print(current_node)
            new_cost = path_cost[current_node] + g_path[(current_node, neighbour)]
            if neighbour not in path_cost or new_cost < path_cost[neighbour]:
                path_cost[neighbour] = new_cost
                total = new_cost + est_distance(M, neighbour, goal)
                frontier_nodes.put(neighbour, total)
                path[neighbour] = current_node
    
#     overall_cost = path_cost[goal]
    final_path = find_path_recursive(path, goal)
    
#     return final_path, overall_cost
    return final_path