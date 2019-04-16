from DFS import DFSGraph


def topological_sorting(graph):
    path = graph.dfs()
    return path


def main():
    graph = DFSGraph()
    graph.add_edge(21, 211)
    graph.add_edge(211, 711)
    graph.add_edge(11, 21)
    graph.add_edge(71, 211)
    graph.add_edge(21, 271)
    graph.add_edge(271, 711)
    path = topological_sorting(graph)
    for vertex in path:
        print(vertex)


if __name__ == '__main__':
    main()
