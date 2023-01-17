def four_neighbor_function(node: any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]


# bfs algorithm
def breadth_first_search(start=(-1, -1), end=(2, 1), neighbor_function=four_neighbor_function):
    """
            >>> breadth_first_search(start=(1,1),end=(2,2))
            [(1,1), (1, 2), (2, 2)]
            >>> breadth_first_search(start=(0,0),end=(2,2))
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
            >>> breadth_first_search(start=(0,0),end=(6,6))
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
             >>> breadth_first_search(start=(-1,-1),end=(3,3))
            [(-1, -2), (0, -2), (1, -2), (2, -2), (3, -2), (3, -1), (3, 0), (3, 1), (3, 2), (3, 3)]
        """
    queue = []
    prev = {}
    queue.append(start)
    visited = [start]  # check the nodes that we visited
    while queue:
        curr = queue.pop(0)  # v0
        ans = neighbor_function(curr)
        if curr == end:  # if is the same node
            return get_path(prev, start, end)
        for i in ans:
            if i not in visited:  # and we didn't visit him
                visited.append(i)
                queue.append(i)
                prev[i] = curr

                # go from the final to the start, and add the vertex to the list


def get_path(path, start, end):
    list_of_path = [end]
    current = path[end]
    while current != start:  # while we didn't finish
        list_of_path.append(current)
        current = path[current]
    list_of_path.append(start)
    new_list = []
    for i in reversed(list_of_path):
        new_list.append(i)
    return new_list


if __name__ == '__main__':
    # test case#

    print("1. start=(1,-1) end=(-2,2)")
    print("   the res is : ", breadth_first_search(start=(1, -1), end=(-2, 2)), "\n")
    print("2. start=(-5,-5) end=(4,4)")
    print("   the res is : ", breadth_first_search(start=(-5, -5), end=(4, 4)), "\n")
    print("3. start=(-1,-1) end=(1,1)")
    print("   the res is : ", breadth_first_search(start=(-1, -1), end=(1, 1)), "\n")
    print("4. start=(0,0) end=(2,2)")
    print("   the res is : ", breadth_first_search(start=(0, 0), end=(2, 2)), "\n")
    print("5. start=(3,-6) end=(4,2)")
    print("   the res is : ", breadth_first_search(start=(3, -6), end=(4, 2)), "\n")
    print("6. start=(0, 0) end=(10, 10)")
    print("   the res is : ", breadth_first_search(start=(0, 0), end=(10, 10)), "\n")
