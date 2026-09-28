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
