def union(p, q, fathers, nodes):
    p_root = find(p, fathers, nodes)
    q_root = find(q, fathers, nodes)
    if p_root != q_root:
        fathers[p_root] = q_root
        nodes[q_root] |= nodes[p_root]


def find(p, fathers, nodes):
    while p != fathers[p]:
        nodes[fathers[p]] |= nodes[p]

        p = fathers[p]
    return p


def solution(connects, n):
    connect_map = [set([i]) for i in range(n + 1)]

    fathers = [i for i in range(n + 1)]

    nodes = [None] + [set([i + 1]) for i in range(n)]

    for connect in connects:
        p = connect[0]
        q = connect[1]

        connect_map[p].add(q)
        union(p, q, fathers, nodes)
    
    result = set()
    for i in range(1, len(nodes)):
        if len(nodes[i]) == n:
            result |= connect_map[i]
    # print(connect_map)
    # print(nodes)
    return len(result)


import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    connections = []

    pairs = list(map(int, sys.stdin.readline().strip().split(' ')))
    for i in range(0, len(pairs), 2):
        connections.append((pairs[i], pairs[i + 1]))

    print(solution(connections, n))