class Graph:
    def __init__(self):
        self._vertices = 0
        self._adjacent_list = {}

    def add_vertex(self, vertex):
        if vertex in self._adjacent_list:
            return

        self._adjacent_list[vertex] = []
        self._vertices += 1

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self._adjacent_list or vertex2 not in self._adjacent_list:
            return

        self._adjacent_list[vertex1].append(vertex2)
        self._adjacent_list[vertex2].append(vertex1)

    def show(self):
        for vertex in self._adjacent_list:
            print(f"{vertex} --> {self._adjacent_list[vertex]}")

def main():
    graph = Graph()

    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)

    graph.show()

if __name__ == "__main__":
    main()
                