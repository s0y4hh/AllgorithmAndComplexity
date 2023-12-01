import networkx as nx
import matplotlib.pyplot as plt

def maximum_matching_bipartite_graph(graph):
    """
    Finds the maximum matching in a bipartite graph using the Hopcroft-Karp algorithm.

    Parameters:
    graph (NetworkX bipartite graph): The bipartite graph on which to find the maximum matching.

    Returns:
    dict: A dictionary representing the maximum matching, where the keys are vertices from the right set
        and the values are the corresponding vertices from the left set.
    """
    # Rest of the code...
def maximum_matching_bipartite_graph(graph):
    # This function is an implementation of the Hopcroft-Karp algorithm for finding maximum matching in bipartite graphs
    # The graph parameter should be a NetworkX bipartite graph

    # Perform BFS to find the distance from unmatched vertices to the root
    def bfs():
        queue = [u for u in left_set if u not in matching]
        distance.update({u: 0 for u in queue})
        while queue:
            u = queue.pop(0)
            for v in graph.neighbors(u):
                if v not in distance and u != matching.get(v, None):
                    distance[v] = distance[u] + 1
                    if v in right_set:
                        queue.append(v)

    # Use DFS to find an augmenting path
    def dfs(u):
        for v in graph.neighbors(u):
            if v not in visited:
                visited.add(v)
                if v in matching:
                    if distance[u] + 1 == distance[matching[v]] and dfs(matching[v]):
                        matching[v] = u
                        return True
                else:
                    matching[v] = u
                    return True
        return False

    left_set, right_set = nx.bipartite.sets(graph)
    matching = {}
    distance = {}
    while True:
        bfs()
        visited = set()
        augmenting_paths = [dfs(u) for u in left_set if u not in matching]
        if not any(augmenting_paths):
            break

    return matching
# Example: College Admissions
projectRole = ["Programmer", "Documentation", "Presentor"]
groupMember = ["Student1", "Student2", "Student3", "Student4"]

# Create a bipartite graph
bipartiteGraph = nx.Graph()

# Add nodes with the node attribute "bipartite"
bipartiteGraph.add_nodes_from(projectRole, bipartite=0)  # projectRole
bipartiteGraph.add_nodes_from(groupMember, bipartite=1)  # groupMember

# Add edges representing preferences
bipartiteGraph.add_edges_from([
    ("Programmer", "Student1"),
    ("Programmer", "Student2"),
    ("Documentation", "Student1"),
    ("Presentor", "Student3"),
    ("Presentor", "Student2"),
    ("Documentation", "Student4"),
    ("Programmer", "Student3"),
])

def maximum_matching(graph):
    # Initialize an empty matching
    matching = {}

    # Find augmenting  paths and update the matching
    while True:
        # we use depth-first search to find an augmenting path in the graph
        path = find_augmenting_path(graph, matching)
        
        # if no augmenting path is found, break the loop
        if not path:
            break

        # Update the matching based on the augmenting path if one is found
        for i in range(0, len(path), 2):
            matching[path[i]] = path[i + 1]
            matching[path[i + 1]] = path[i]

    return matching

def find_augmenting_path(graph, matching):
    # this is the function that finds an augmenting path in the graph using depth-first search
    visited = set()
    # we start the search from the unmatched vertices in the left set
    for node in graph.nodes():
        if node not in matching and node not in visited:
            path = dfs(graph, node, matching, visited)
            if path:
                return path
    return None

def dfs(graph, current_node, matching, visited):
    # deptgh-first search algorithm for finding an augmenting path in the graph
    visited.add(current_node)

    for neighbor in graph.neighbors(current_node):
        if neighbor not in visited:
            visited.add(neighbor)

            if neighbor not in matching or dfs(graph, matching[neighbor], matching, visited):
                return [current_node, neighbor] + (matching.get(neighbor, []))

    return None

# Find the maximum matching
matching = maximum_matching_bipartite_graph(bipartiteGraph)

# Print the matching result
print("Maximum Matching:")
for college, student in matching.items():
    print(f"{college} - {student}")

# Visualization
pos = {node: (0, i) for i, node in enumerate(projectRole)}
pos.update({node: (1, i) for i, node in enumerate(groupMember)})

# Draw the bipartite graph with matching edges in red
nx.draw(bipartiteGraph, pos, with_labels=True, font_weight='bold', node_color='green', edge_color='gray', node_size=1500)
matching_edges = [(role, student) for role, student in matching.items()]
nx.draw_networkx_edges(bipartiteGraph, pos, edgelist=matching_edges, edge_color='red', width=2)

plt.show()
