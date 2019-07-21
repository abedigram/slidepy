import collections
import problem


def breadth_first_search(start):
    visited, queue, parent = {start}, collections.deque([start]), {start: -1}
    while queue:
        vertex = queue.popleft()
        neighbours = problem.get_children(index=vertex)
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                if problem.is_goal(neighbour):
                    return parent
                queue.append(neighbour)
    return {}


problem.solve(breadth_first_search, problem.get_input())
