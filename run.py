# Search methods

import search

base = search.GPSProblem('A', 'B', search.romania)
ab = search.InstrumentedProblem(base)

algorithms = [
    search.breadth_first_graph_search,
    search.depth_first_graph_search,
    search.branch_and_bound_graph_search,
    search.branch_and_bound_subestimation_graph_search
]

# Loop through each algorithm
for algorithm in algorithms:
    print(f"\n--- {algorithm.__name__} ---") 
    
    print(algorithm(ab).path())
    
    ab.printNodeStats()
    
    ab.clear()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
