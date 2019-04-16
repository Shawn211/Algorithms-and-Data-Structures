from DFS import DFSGraph


def show_scc_transpose_graphs(graph):
    path = graph.dfs()
    transpose_graph = DFSGraph()
    for to_vertex in path:
        for from_vertex in path:
            if to_vertex in from_vertex.get_connections():
                transpose_graph.add_edge(to_vertex.get_id(), from_vertex.get_id())
    transpose_path = transpose_graph.dfs()
    graphs = []
    i = 0
    while i < len(transpose_path):
        first_vertex = transpose_path[i]
        vertex_num = (first_vertex.get_finish() - first_vertex.get_discovery() + 1) // 2
        sub_graph = DFSGraph()
        vertex_list = transpose_path[i: i + vertex_num]
        for from_vertex in vertex_list:
            for to_vertex in vertex_list:
                if to_vertex in from_vertex.get_connections():
                    sub_graph.add_edge(from_vertex.get_id(), to_vertex.get_id())
        graphs.append(sub_graph)
        i += vertex_num
    for i, graph in enumerate(reversed(graphs)):
        print(f'Graph {i + 1}')
        sub_path = graph.dfs()
        for vertex in sub_path:
            print(vertex)


def scc(graph):
    path = graph.dfs()
    transpose_graph = DFSGraph()
    for to_vertex in path:
        for from_vertex in path:
            if to_vertex in from_vertex.get_connections():
                transpose_graph.add_edge(to_vertex.get_id(), from_vertex.get_id())
    transpose_path = transpose_graph.dfs()

    scc_vertex_ids = []
    i = 0
    while i < len(transpose_path):
        first_vertex = transpose_path[i]
        vertex_num = (first_vertex.get_finish() - first_vertex.get_discovery() + 1) // 2
        scc_vertex_ids.append([vertex.get_id() for vertex in transpose_path[i: i + vertex_num]])
        i += vertex_num
    return list(reversed(scc_vertex_ids))


def main():
    graph = DFSGraph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'F')
    graph.add_edge('F', 'H')
    graph.add_edge('H', 'I')
    graph.add_edge('I', 'F')
    graph.add_edge('C', 'C')
    graph.add_edge('B', 'E')
    graph.add_edge('E', 'D')
    graph.add_edge('D', 'G')
    graph.add_edge('G', 'E')
    graph.add_edge('D', 'B')
    graph.add_edge('E', 'A')
    print(scc(graph))
    show_scc_transpose_graphs(graph)


if __name__ == '__main__':
    main()
