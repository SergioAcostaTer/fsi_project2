import search
import time

base = search.GPSProblem('A', 'B', search.romania)

algorithms = [
    search.breadth_first_graph_search,
    search.depth_first_graph_search,
    search.branch_and_bound_graph_search,
    search.branch_and_bound_subestimation_graph_search
]

print(f"Problem: Start {base.initial} -> Goal {base.goal}\n")

def run_algorithm(algorithm, base_problem):
    problem = search.InstrumentedProblem(base_problem)
    
    start = time.time()
    result = algorithm(problem)
    end = time.time()
    
    if result:
        path = str(result.path())
        cost = result.path_cost
    else:
        path = "No solution"
        cost = 0
        
    return [
        algorithm.__name__,
        problem.generated,
        problem.visited,
        cost,
        f"{end - start:.6f}",
        path
    ]

header = ["Algorithm", "Generated", "Visited", "Cost", "Time (s)", "Path"]
data = []

for algo in algorithms:
    data.append(run_algorithm(algo, base))

search.print_table(data, header=header, sep=' | ')

# Reference Results:
# BFS: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] (Cost: 418)
# DFS: [<Node B>, <Node F>, <Node S>, <Node A>] (Cost: 450)