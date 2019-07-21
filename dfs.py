import problem

def dfs(start):
    visited, stack, parent = set(), [start], {start: -1}
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            neighbors = problem.get_children(index=vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    if problem.is_goal(neighbor):
                        return parent
                    stack.append(neighbor)

            # stack.extend(graph[vertex] - visited)
    return {}

problem.solve(dfs, problem.get_input())
