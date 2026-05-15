from collections import deque
import heapq


class Solver:

    @staticmethod
    def _neighbors(current):

        x, y = current

        return [
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1)
        ]

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

            for nx, ny in Solver._neighbors(current):

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

            for nx, ny in Solver._neighbors(current):

                if (
                    maze.is_walkable(nx, ny)
                    and (nx, ny) not in visited
                ):

                    visited.add((nx, ny))
                    stack.append((nx, ny))

        return traversal

    @staticmethod
    def dijkstra(maze, start, goal):

        priority_queue = [(0, start)]
        best_cost = {start: 0}
        visited = set()
        traversal = []

        while priority_queue:

            current_cost, current = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)
            traversal.append(current)

            if current == goal:
                break

            for nx, ny in Solver._neighbors(current):

                neighbor = (nx, ny)

                if not maze.is_walkable(nx, ny):
                    continue

                new_cost = current_cost + maze.get_movement_cost(nx, ny)

                if new_cost < best_cost.get(neighbor, float("inf")):
                    best_cost[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return traversal

    @staticmethod
    def _manhattan_distance(current, goal):

        current_x, current_y = current
        goal_x, goal_y = goal

        return abs(current_x - goal_x) + abs(current_y - goal_y)

    @staticmethod
    def greedy_best_first_search(maze, start, goal):

        priority_queue = [(Solver._manhattan_distance(start, goal), start)]
        visited = set()
        visited.add(start)
        traversal = []

        while priority_queue:

            _, current = heapq.heappop(priority_queue)

            traversal.append(current)

            if current == goal:
                break

            for nx, ny in Solver._neighbors(current):

                neighbor = (nx, ny)

                if (
                    maze.is_walkable(nx, ny)
                    and neighbor not in visited
                ):

                    visited.add(neighbor)
                    priority = Solver._manhattan_distance(neighbor, goal)
                    heapq.heappush(priority_queue, (priority, neighbor))

        return traversal
