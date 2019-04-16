from Graph import Graph
from KnightGraph import position_to_key, generate_legal_moves


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.set_color('white')
            vertex.set_predecessor(None)
        path = []
        for vertex in self:
                if vertex.get_color() == 'white':
                    self.dfs_visit(vertex, path)
        return list(reversed(path))

    def dfs_visit(self, vertex, path):
        vertex.set_color('gray')
        self.time += 1
        vertex.set_discovery(self.time)
        for neighbor in vertex.get_connections():
            if neighbor.get_color() == 'white':
                self.dfs_visit(neighbor, path)
                neighbor.set_predecessor(vertex)
        vertex.set_color('black')
        path.append(vertex)
        self.time += 1
        vertex.set_finish(self.time)


def knight_dfs_graph(board_size):
    dfs_graph = DFSGraph()
    for row in range(board_size):
        for column in range(board_size):
            from_key = position_to_key(row, column, board_size)
            to_key_positions = generate_legal_moves(row, column, board_size)
            for to_key_position in to_key_positions:
                to_key = position_to_key(to_key_position[0], to_key_position[1], board_size)
                dfs_graph.add_edge(from_key, to_key)
    return dfs_graph


def show_discovery_finish_time(graph):
    board_size = int(len(graph.get_vertices()) ** 0.5)
    for row in range(board_size):
        for column in range(board_size):
            vertex = graph.get_vertex(row * board_size + column)
            discovery = str(vertex.get_discovery())
            finish = str(vertex.get_finish())
            while len(discovery) < 2:
                discovery = ' ' + discovery
            while len(finish) < 2:
                finish = ' ' + finish
            discovery_finish_str = discovery + '/' + finish
            if column != board_size - 1:
                print(discovery_finish_str, end=' ')
            else:
                print(discovery_finish_str, end='')
        print()


def main():
    # 构建骑士游历图
    board_size = 6
    graph = knight_dfs_graph(board_size)
    # 深度优先搜索获取骑士游历棋盘各点发现时间和完成时间
    graph.dfs()
    # 展示骑士游历各点发现时间和完成时间棋盘
    show_discovery_finish_time(graph)


if __name__ == '__main__':
    main()
