import problem


def ldfs(start, limit=4):
    visited, stack, parent = set(), [(start, 0)], {start: -1}
    while stack:
        vertex, depth = stack.pop()
        if vertex not in visited and depth < limit:
            visited.add(vertex)
            neighbors = problem.get_children(index=vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    if problem.is_goal(neighbor):
                        return parent
                    stack.append((neighbor, depth + 1))

            # stack.extend(graph[vertex] - visited)
    return {}


problem.solve(ldfs, problem.get_input())
