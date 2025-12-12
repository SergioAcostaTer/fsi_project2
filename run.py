# Search methods

import search
import time

base = search.GPSProblem('A', 'B', search.romania)
ab = search.InstrumentedProblem(base)

algorithms = [
    search.breadth_first_graph_search,
    search.depth_first_graph_search,
    search.branch_and_bound_graph_search,
    search.branch_and_bound_subestimation_graph_search
]

header = ["Algorithm", "Generated", "Visited", "Cost", "Time (s)", "Path"]
data = []

print(f"Problem: Start {base.initial} -> Goal {base.goal}\n")

for algorithm in algorithms:
    start_time = time.time()
    result = algorithm(ab)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    if result:
        path_str = str(result.path()) 
        cost = result.path_cost
    else:
        path_str = "No solution"
        cost = 0
        
    generated = ab.generated
    visited = ab.visited
    
    data.append([
        algorithm.__name__, 
        generated, 
        visited, 
        cost, 
        f"{elapsed_time:.6f}", 
        path_str
    ])
    
    ab.clear()

search.print_table(data, header=header, sep=' | ')

# Result Reference (from previous runs):
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
