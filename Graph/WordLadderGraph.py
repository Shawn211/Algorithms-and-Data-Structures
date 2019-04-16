from Graph import Graph


def word_ladder_graph(word_list):
    graph = Graph()
    bucket_words_dict = dict()

    for word in word_list:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in bucket_words_dict:
                bucket_words_dict[bucket].append(word)
            else:
                bucket_words_dict[bucket] = [word]

    for bucket in bucket_words_dict.keys():
        for from_word in bucket_words_dict[bucket]:
            for to_word in bucket_words_dict[bucket]:
                if from_word != to_word:
                    graph.add_edge(from_word, to_word)
    return graph


def main():
    words = ['21', '211', '271', '711']
    graph = word_ladder_graph(words)
    for from_vertex in graph:
        print(from_vertex)


if __name__ == '__main__':
    main()
