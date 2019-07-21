import problem

final = problem.get_index(problem.state)


def bid(start):
    if start == final:
        return [start]
    active_vertices_path_dict = {start: [start], final: [final]}
    inactive_vertices = set()

    while len(active_vertices_path_dict) > 0:

        active_vertices = list(active_vertices_path_dict.keys())
        for vertex in active_vertices:
            current_path = active_vertices_path_dict[vertex]
            origin = current_path[0]
            current_neighbours = set(problem.get_children(vertex)) - inactive_vertices
            if len(current_neighbours.intersection(active_vertices)) > 0:
                for meeting_vertex in current_neighbours.intersection(active_vertices):
                    if origin != active_vertices_path_dict[meeting_vertex][0]:
                        active_vertices_path_dict[meeting_vertex].reverse()
                        return active_vertices_path_dict[vertex] + active_vertices_path_dict[meeting_vertex]

            if len(set(current_neighbours) - inactive_vertices - set(active_vertices))  == 0:
                active_vertices_path_dict.pop(vertex, None)
                inactive_vertices.add(vertex)
            else:
                for neighbour_vertex in current_neighbours - inactive_vertices - set(active_vertices):
                    active_vertices_path_dict[neighbour_vertex] = current_path + [neighbour_vertex]
                    active_vertices.append(neighbour_vertex)
                active_vertices_path_dict.pop(vertex, None)
                inactive_vertices.add(vertex)

problem.solve(bid, problem.get_input(), True)