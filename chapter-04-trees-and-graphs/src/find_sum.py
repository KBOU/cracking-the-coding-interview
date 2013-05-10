# coding: utf-8

def find_sum_helpler(node, sm, path, level):
    if node is None:
        return

    path[level] = node.data

    t = 0
    for i in range(level, -1, -1):
        t += path[i]
        if t == sm:
            print_path(path, i, level)

    
    find_sum_helpler(node.left, sm, path, level+1)
    find_sum_helpler(node.right, sm, path, level+1)

    path[level] = -sys.maxint - 1

def print_path(path, start, end):
    for i in range(start, end+1):
        print str(path[i]) + " ",

    print

def depth(node):
    if node is None:
        return 0
    return 1 + max(depth(node.left), depth(node.right))

def find_sum(node, sm):
    d = depth(node)
    path = [0] * d
    find_sum_helper(node, sm, path, 0)

