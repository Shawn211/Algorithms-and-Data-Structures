class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.vertices_num = 0

    def add_vertex(self, key):
        self.vertices_num += 1
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertex_dict

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertex_dict:
            self.add_vertex(from_key)
        if to_key not in self.vertex_dict:
            self.add_vertex(to_key)
        self.vertex_dict[from_key].add_neighbor(self.vertex_dict[to_key], weight)

    def get_vertices(self):
        return self.vertex_dict.keys()

    def __iter__(self):
        return iter(self.vertex_dict.values())


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

        self.distance = 0
        self.predecessor = None
        self.color = 'white'

        self.discovery_time = 0
        self.finish_time = 0

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([v.id for v in self.connected_to])

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_predecessor(self):
        return self.predecessor

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_discovery(self, time):
        self.discovery_time = time

    def get_discovery(self):
        return self.discovery_time

    def set_finish(self, time):
        self.finish_time = time

    def get_finish(self):
        return self.finish_time


def main():
    graph = Graph()
    for i in range(2):
        graph.add_vertex(i)

    print(graph.vertex_dict)

    graph.add_edge(0, 1, 2)
    graph.add_edge(1, 2, 7)
    graph.add_edge(2, 0, 1)

    for from_vertex in graph:
        print(from_vertex)


if __name__ == '__main__':
    main()
