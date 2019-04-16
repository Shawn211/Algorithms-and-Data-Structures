from WordLadderGraph import word_ladder_graph
from Queue import Queue


def bfs(graph, start_key, end_key):
    vertex_queue = Queue()
    start_vertex = graph.get_vertex(start_key)
    end_vertex = graph.get_vertex(end_key)

    start_vertex.set_color('gray')
    vertex_queue.enqueue(start_vertex)
    while not vertex_queue.is_empty():
        current_vertex = vertex_queue.dequeue()
        for neighbor in current_vertex.get_connections():
            if neighbor.get_color() == 'white':
                neighbor.set_distance(current_vertex.get_distance() + 1)
                neighbor.set_predecessor(current_vertex)
                neighbor.set_color('gray')
                if neighbor == end_vertex:
                    return neighbor
                vertex_queue.enqueue(neighbor)
        current_vertex.set_color('black')


def traverse(vertex):
    current_vertex = vertex
    while current_vertex.get_predecessor():
        print(current_vertex.get_id())
        current_vertex = current_vertex.get_predecessor()
    print(current_vertex.get_id())


def main():
    words = ['21', '211', '271', '711']
    graph = word_ladder_graph(words)
    end_vertex = bfs(graph, '271', '711')
    traverse(end_vertex)


if __name__ == '__main__':
    main()
