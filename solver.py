from collections import deque

class Solver:

    @staticmethod
    def bfs(maze, start, goal):

        queue = deque([start])

        visited = set()
        visited.add(start)

        traversal = []

        while queue:

            current = queue.popleft()

            traversal.append(current)

            if current == goal:
                break

            x, y = current

            neighbors = [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1)
            ]

            for nx, ny in neighbors:

                if (
                    maze.is_walkable(nx, ny)
                    and (nx, ny) not in visited
                ):

                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return traversal

    @staticmethod
    def dfs(maze, start, goal):

        stack = [start]

        visited = set()
        visited.add(start)

        traversal = []

        while stack:

            current = stack.pop()

            traversal.append(current)

            if current == goal:
                break

            x, y = current

            neighbors = [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1)
            ]

            for nx, ny in neighbors:

                if (
                    maze.is_walkable(nx, ny)
                    and (nx, ny) not in visited
                ):

                    visited.add((nx, ny))
                    stack.append((nx, ny))

        return traversal