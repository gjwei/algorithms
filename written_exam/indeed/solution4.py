#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Author: gjwei

cur_keys = set()
cur_keys.add(0)


def bfs(room_links, row_id, reach_rooms):
    may_reach_rooms = room_links[row_id]

    for (v, k) in may_reach_rooms:
        if k in cur_keys:
            cur_keys.add(v)
            reach_rooms.add(v)
            bfs(room_links, v, reach_rooms)
    return


if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    rooms = [[] for _ in range(N)]

    for _ in range(M):
        u, v, k = map(int, input().split(' '))
        rooms[u - 1].append((v - 1, k - 1))

    reach_rooms = set()
    reach_rooms.add(0)

    bfs(rooms, 0, reach_rooms)
    print(len(reach_rooms))



