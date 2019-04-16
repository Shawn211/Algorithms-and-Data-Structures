from Graph import Graph


def knight_graph(board_size):
    graph = Graph()
    for row in range(board_size):
        for column in range(board_size):
            from_key = position_to_key(row, column, board_size)
            to_key_positions = generate_legal_moves(row, column, board_size)
            for to_key_position in to_key_positions:
                to_key = position_to_key(to_key_position[0], to_key_position[1], board_size)
                graph.add_edge(from_key, to_key)
    return graph


def position_to_key(row, column, board_size):
    return (row * board_size) + column


def generate_legal_moves(row, column, board_size):
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

    for move_offset in move_offsets:
        new_x = row + move_offset[0]
        new_y = column + move_offset[1]
        if is_legal_coord(new_x, board_size) and is_legal_coord(new_y, board_size):
            new_moves.append((new_x, new_y))
    return new_moves


def is_legal_coord(coord, board_size):
    if 0 <= coord < board_size:
        return True
    else:
        return False


def main():
    graph = knight_graph(3)
    for from_vertex in graph:
        print(from_vertex)


if __name__ == '__main__':
    main()
