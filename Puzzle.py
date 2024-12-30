from collections import deque

# All code is my own, I have included citations where relevant


def solve_puzzle(Board, Source, Destination):
    """
    This function takes in a 2D array and a Source and Destination node and finds the minimum path between the two nodes.
    Critically, this is a 2D array with obstacles, represented as '#', across which the traversal may not cross.
    """

    if Source == Destination:  # Base case, we are already at the destination
        return [Source]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    direction_str = {
        (0, 1): 'R',
        (1, 0): 'D',
        (0, -1): 'L',
        (-1, 0): 'U'
        }
    visited = set()  # Why set()? Because each item MUST BE UNIQUE

    queue = deque([Source])  # Enqueue our starting node, Source
    visited.add(Source)  # Add source to visited set
    prev_node = {}  # Create Dict object to hold visited nodes and their parent/previous node

    # While loop Adapted from: https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/
    # Author: None that I can see? But it does say 'code contributed by sajalmittaldei'
    # Accessed: 11/28/2024

    while len(queue) > 0 and False not in visited:      # While our queue is not empty and we have not traversed every node...
        s = queue.popleft()     # Pop the left end of the queue. We are doing a FIFO queue.

        if s == Destination:    # If we are at our destination, stop searching
            break

        for x, y in directions:     # Iterate through our directions array

            # This next part is important: x and y are essentially flipped due to the nature of arrays. So, the first
            # element in a vertex is how deep in the graph/board you should look, and the second element
            # is how far across you should move.

            dx, dy = (s[1] + y), (s[0] + x)

            # If the neighbors are valid, append them to the queue
            if 0 <= dy < len(Board) and 0 <= dx < len(Board[0]) and (dy, dx) not in visited and Board[dy][dx] != '#':
                queue.append((dy, dx))
                visited.add((dy, dx))   # Add neighbor to visited queue
                prev_node[(dy, dx)] = s     # Keep track of node prior to neighbor (so our current node s = neighbor parent)

    # If we could NOT reach our destination, return None
    if Destination not in prev_node:
        return None

    # Backtracking functionality adapted from Response found at:
    # https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
    # Author: qiao - https://stackoverflow.com/users/2702262/qiao
    # Accessed: 11/28/2024

    # Otherwise, to get the path, we have to move backwards through our prev_node array from Destination to Source
    min_path = [Destination]
    while min_path[-1] != Source:
        min_path.append(prev_node[min_path[-1]])

    # Since we moved backwards, we have to now reverse our path
    min_path.reverse()

    # Now we handle the letters part/extra credit
    # Remember that directions are reversed! (Handled in our dir_str dict)
    letter_path = ''
    for move in range(1, len(min_path)):
        dm, dn = min_path[move]
        d2, d1 = min_path[move - 1]

        delta_x = dm - d2
        delta_y = dn - d1
        letter_path += direction_str[(delta_x, delta_y)]

    return (min_path, letter_path)

Puzzle = [
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '#', '#', '-'],
['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0, 2), (2, 2)))


