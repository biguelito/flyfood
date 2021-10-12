import timeit

def possibilites(v):
        if len(v) == 0:
            return []

        if len(v) == 1:
            return [v]

        path = []
        for i in range(len(v)):
            a = v[i]
            remV = v[:i] + v[i+1:]

            for poss in possibilites(remV):
                path.append([a] + poss)
        return path

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

    return

def all_paths(v):



    return

def main():
    l = ['a', 'b', 'c']    
    # [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]
    
    start = timeit.default_timer()
    p = possibilites(l)
    print('possibilites: ', timeit.default_timer() - start)

    # start = timeit.default_timer()
    # ap = all_perms(l)
    # print('all_perms: ', timeit.default_timer() - start)

    r = all_paths(l)
    print(r)

if __name__ == "__main__":
    main()