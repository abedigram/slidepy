import problem
import ldfs


def idfs(start):
    limit = 1
    while True:
        ret = ldfs.ldfs(start, limit)
        if ret == {}:
            limit += 1
        else:
            print(limit)
            return ret


problem.solve(idfs, problem.get_input())
