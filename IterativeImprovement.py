"""
GROUP 8
- Asi Neo Garcia
- Jayson Asiado
- Vohn Ayuban
- Marivel Regaspi
"""

# import the required libraries and modules
# networkx is to create and manipulate graphs and networks
import networkx as nx # set the alias for networkx to nx
import matplotlib.pyplot as plt # set the alias for matplotlib.pyplot to plt

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
        """
        This line creates a list called queue using a list comprehension. 
        It iterates over elements u in the left_set and includes u in the
        list only if u is not in the matching list.
        """
        queue = [u for u in left_set if u not in matching]
        distance.update({u: 0 for u in queue})

        while queue: # while queue is not empty
            u = queue.pop(0) # pop the first element from the queue
            for v in graph.neighbors(u): # iterate over the neighbors of u
                if v not in distance and u != matching.get(v, None): # if v is not in distance and u is not the matching vertex of v
                    distance[v] = distance[u] + 1 # set the distance of v to the distance of u plus 1
                    if v in right_set: # if v is in the right set (EX. v is unmatched) add v to the queue
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
# Example: PROJECT ROLE ASSIGNMENT OF STUDENTS IN DATA STRUCTURES AND ALGORITHMS LEARNING TASK

"""
SINCE THE PROJECT ROLE IS ONLY LIMITED TO 3 ROLES,
THAT THERE WILL BE 1 PROJECT ROLE TO BE ASSIGNED TO 2 STUDENTS
"""
projectRole = ["Programmer", "Documentation", "Presentor"]
groupMember = ["Student1", "Student2", "Student3", "Student4"]

# Create a bipartite graph
bipartiteGraph = nx.Graph()

# Add nodes with the node attribute "bipartite"
bipartiteGraph.add_nodes_from(projectRole, bipartite=0)  # projectRole 
bipartiteGraph.add_nodes_from(groupMember, bipartite=1)  # groupMember

# Add edges between nodes of opposite node sets
bipartiteGraph.add_edges_from([
    ("Programmer", "Student1"),
    ("Programmer", "Student2"),
    ("Documentation", "Student1"),
    ("Documentation", "Student2"),
    ("Presentor", "Student3"),
    ("Presentor", "Student2"),
    ("Presentor", "Student4"),
    ("Programmer", "Student4"),
    ("Programmer", "Student3"),
]) 

# Find the maximum matching
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
        for i in range(0, len(path), 2): # iterate over the path by 2 steps
            matching[path[i]] = path[i + 1] # set the matching of the current node to the next node
            matching[path[i + 1]] = path[i] # set the matching of the next node to the current node

    return matching # return the matching dictionary containing the maximum matched vertices

def find_augmenting_path(graph, matching):
    # this is the function that finds an augmenting path in the graph using depth-first search
    visited = set()
    # we start the search from the unmatched vertices in the left set
    for node in graph.nodes(): # iterate over the nodes in the graph
        if node not in matching and node not in visited: # if the node is not in the matching and not visited
            path = dfs(graph, node, matching, visited) # find the augmenting path using depth-first search
            if path: # if the path is not None,
                return path # return the path
    return None # else return None

def dfs(graph, current_node, matching, visited):
    # deptgh-first search algorithm for finding an augmenting path in the graph
    visited.add(current_node) # add the current node to the visited set

    for neighbor in graph.neighbors(current_node): # iterate over the neighbors of the current node
        if neighbor not in visited: # if the neighbor node is not in visited set then visit it
            visited.add(neighbor) # add the neighbor to the visited set

            if neighbor not in matching or dfs(graph, matching[neighbor], matching, visited): # if the neighbor is not in thematching or the dfs function returns True
                return [current_node, neighbor] + (matching.get(neighbor, [])) # return the path

    return None # else reutne None

# Find the maximum matching in the bipartite graph using the maximum_matching_bipartite_graph function and set the parameter to bipartiteGraph
matching = maximum_matching_bipartite_graph(bipartiteGraph)

# Print the matching result
print("Maximum Matching:")
for college, student in matching.items(): # iterate over the matching dictionary and print the result as the format below
    print(f"{college} - {student}")

# Visualization
pos = {node: (0, i) for i, node in enumerate(groupMember)} # set the position of the nodes in the left set
pos.update({node: (1, i) for i, node in enumerate(projectRole)})   # set the position of the nodes in the right set

# Draw the bipartite graph with matching edges in red
# The nodes in the left set and right set are colored green
nx.draw(bipartiteGraph, pos, with_labels=True, font_weight='bold', node_color='green', edge_color='gray', node_size=1500) # draw the bipartite graph 
matching_edges = [(role, student) for role, student in matching.items()] # set the matching edges to the matching dictionary

# Draw the matching edges in red and with width 2 
nx.draw_networkx_edges(bipartiteGraph, pos, edgelist=matching_edges, edge_color='red', width=2) 

# Show the plot of the bipartite graph
plt.show()

