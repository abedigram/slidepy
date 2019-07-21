import problem


def Astar(start):
   finish = problem.get_index(problem.state)
   pathstorage = [[problem.get_manhatan_heuristic(start), start]]  # optional: heuristic_1
   expanded = []
   expanded_nodes = 0
   while pathstorage:
       i = 0
       for j in range(1, len(pathstorage)):
           if pathstorage[i][0] > pathstorage[j][0]:
               i = j
       path = pathstorage[i]
       pathstorage = pathstorage[:i] + pathstorage[i + 1:]
       finishnode = path[-1]
       if finishnode == finish:
           break
       if finishnode in expanded: continue
       children = problem.get_children(finishnode)
       for b in children:
           if b in expanded: continue
           newpath = [path[0] + problem.get_manhatan_heuristic(b) - problem.get_manhatan_heuristic(finishnode)] + path[1:] + [b]
           pathstorage.append(newpath)
           expanded.append(finishnode)
       expanded_nodes += 1
   return path[1:]


problem.solve(Astar, problem.get_input(), has_path=True, should_reverse=False)
