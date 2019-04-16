from KnightGraph import knight_graph


def knight_tour(depth, path, vertex, limit):
    vertex.set_color('gray')
    path.append(vertex)
    if depth < limit:
        neighbors = order_by_available_moves(vertex)
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].get_color() == 'white':
                done = knight_tour(depth + 1, path, neighbors[i], limit)
            i += 1
        if not done:
            path.pop()
            vertex.set_color('white')
    else:
        done = True
    return done


def order_by_available_moves(vertex):
    neighbor_moves_list = []
    for neighbor in vertex.get_connections():
        if neighbor.get_color() == 'white':
            available_moves_num = 0
            for great_neighbor in neighbor.get_connections():
                if great_neighbor.get_color() == 'white':
                    available_moves_num += 1
            neighbor_moves_list.append((available_moves_num, neighbor))

    neighbor_moves_list.sort(key=lambda x: x[0])
    sorted_neighbors = [neighbor_moves[1] for neighbor_moves in neighbor_moves_list]
    return sorted_neighbors


def show_move_board(path):
    board_size = int(len(path) ** 0.5)
    path_keys = [vertex.get_id() for vertex in path]
    for row in range(board_size):
        for column in range(board_size):
            step_num = str(path_keys.index(row * board_size + column))
            while len(step_num) < 2:
                step_num = ' ' + step_num
            if column != board_size - 1:
                print(step_num, end=' ')
            else:
                print(step_num, end='')
        if row != board_size - 1:
            print()


def main():
    # 构建骑士游历图
    board_size, start_key = 6, 6
    graph = knight_graph(board_size)
    # 设置骑士游历参数值
    depth = 1
    path = []
    start_vertex = graph.get_vertex(start_key)
    limit = board_size ** 2
    # 获取骑士游历结果
    print(knight_tour(depth, path, start_vertex, limit))
    # 展示骑士游历移动棋盘
    show_move_board(path)


if __name__ == '__main__':
    main()
