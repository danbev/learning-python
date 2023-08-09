from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, n):
        # Default dictionary is similar to a normal dictionary except that it
        # has a default value if a key has not been assigned a value. S in this
        # case list is the factor function and if index being added does not
        # exist then it will create a new list.
        self.graph = defaultdict(list)
        self.N = n

    def addEdge(self, m, n):
        self.graph[m].append(n)

    def _sort(self, n, visited, stack):
        visited[n] = True
        for element in self.graph[n]:
            if visited[element] == False:
                self._sort(element, visited, stack)

        stack.insert(0, n)

    def sort(self):
        # The following creates a list of one boolean False value and then
        # multiplies it by the number of nodes in the graph.
        visited = [False] * self.N
        print(f'visited: {visited}')
        stack = []

        for element in range(self.N):
            if visited[element] == False:
                self._sort(element, visited, stack)

        return stack

graph = Graph(5)
graph.addEdge(0,1);
graph.addEdge(0,3);
graph.addEdge(1,2);
graph.addEdge(2,3);
graph.addEdge(2,4);
graph.addEdge(3,4);
print(f'Topological sort: {graph.sort()}')

# Create a Directed Graph
G = nx.DiGraph()

# Add nodes and edges to the graph (Creating a DAG)
G.add_edges_from([(0, 1), (0, 3), (1, 2), (2, 3), (2, 4), (3, 4)])

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue")
plt.title("Directed Acyclic Graph (DAG)")
plt.show()

