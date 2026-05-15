import random
import pygame
from pathlib import Path

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (100, 100, 100)
BLUE = (80, 140, 255)
YELLOW = (255, 220, 100)
GREEN = (100, 255, 100)
BROWN = (120, 80, 45)

CELL_SIZE = 50
OFFSET_X = 150
OFFSET_Y = 80
SOURCE_TILE_SIZE = 16
TILESET_PATH = Path(__file__).with_name("stone_to_void.png")

FLOOR = 0
WALL = 1
MUD = 2

FLOOR_TILE_POSITION = (1, 1)
WALL_TILE_POSITION = (0, 4)
MUD_TILE_POSITION = (1, 4)

FLOOR_COST = 1
MUD_COST = 5

WALL_CHANCE = 0.25
MUD_CHANCE = 0.15


goal_reached = False


class Maze:

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        self.grid = []

        self.font = pygame.font.SysFont(None, 36)
        self.tiles = self._load_tiles()

        self.generate()

    def _load_tiles(self):

        if not TILESET_PATH.exists():
            return {}

        tileset = pygame.image.load(str(TILESET_PATH))

        if pygame.display.get_surface():
            tileset = tileset.convert_alpha()

        return {
            "wall": self._load_tile(tileset, WALL_TILE_POSITION),
            "floor": self._load_tile(tileset, FLOOR_TILE_POSITION),
            "mud": self._load_tile(tileset, MUD_TILE_POSITION),
        }

    def _load_tile(self, tileset, atlas_position):

        atlas_x, atlas_y = atlas_position
        tile_rect = pygame.Rect(
            atlas_x * SOURCE_TILE_SIZE,
            atlas_y * SOURCE_TILE_SIZE,
            SOURCE_TILE_SIZE,
            SOURCE_TILE_SIZE
        )

        if not tileset.get_rect().contains(tile_rect):
            return None

        tile = tileset.subsurface(tile_rect).copy()
        return pygame.transform.scale(tile, (CELL_SIZE, CELL_SIZE))

    def generate(self):

        max_attempts = 100

        for _ in range(max_attempts):

            self.grid = self._generate_random_grid()

            if self._has_solution():
                return

        self.grid = self._generate_fallback_grid()

    def _generate_random_grid(self):

        grid = []

        for y in range(self.rows):

            row = []

            for x in range(self.cols):

                if (x == 0 and y == 0) or (
                    x == self.cols - 1 and y == self.rows - 1
                ):
                    row.append(FLOOR)

                else:
                    roll = random.random()

                    if roll < WALL_CHANCE:
                        row.append(WALL)
                    elif roll < WALL_CHANCE + MUD_CHANCE:
                        row.append(MUD)
                    else:
                        row.append(FLOOR)

            grid.append(row)

        return grid

    def _generate_fallback_grid(self):

        grid = [[WALL for _ in range(self.cols)] for _ in range(self.rows)]

        for x in range(self.cols):
            grid[0][x] = FLOOR

        for y in range(self.rows):
            grid[y][self.cols - 1] = FLOOR

        self._place_fallback_mud(grid)

        return grid

    def _place_fallback_mud(self, grid):

        for x in range(2, self.cols - 1, 3):
            grid[0][x] = MUD

        for y in range(2, self.rows - 1, 3):
            grid[y][self.cols - 1] = MUD

    def _has_solution(self):

        start = (0, 0)
        goal = (self.cols - 1, self.rows - 1)
        stack = [start]
        visited = {start}

        while stack:

            current = stack.pop()

            if current == goal:
                return True

            x, y = current

            for nx, ny in (
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1)
            ):

                if self.is_walkable(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))

        return False

    def is_walkable(self, x, y):

        return (
            0 <= x < self.cols
            and 0 <= y < self.rows
            and self.grid[y][x] != WALL
        )

    def get_movement_cost(self, x, y):

        if not self.is_walkable(x, y):
            return float("inf")

        if self.grid[y][x] == MUD:
            return MUD_COST

        return FLOOR_COST

    def _draw_base_tile(self, screen, rect, tile_type):

        if tile_type == WALL:
            wall_tile = self.tiles.get("wall")

            if wall_tile:
                screen.blit(wall_tile, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

        elif tile_type == MUD:
            mud_tile = self.tiles.get("mud")

            if mud_tile:
                screen.blit(mud_tile, rect)
            else:
                pygame.draw.rect(screen, BROWN, rect)

        else:
            floor_tile = self.tiles.get("floor")

            if floor_tile:
                screen.blit(floor_tile, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

    def draw(self, screen, visited_steps, current_step, goal_reached):

        for y in range(self.rows):

            for x in range(self.cols):

                rect = pygame.Rect(
                    OFFSET_X + x * CELL_SIZE,
                    OFFSET_Y + y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )

                self._draw_base_tile(screen, rect, self.grid[y][x])

                pygame.draw.rect(screen, GRAY, rect, 1)

        for i in range(min(current_step, len(visited_steps))):

            x, y = visited_steps[i]

            rect = pygame.Rect(
                OFFSET_X + x * CELL_SIZE,
                OFFSET_Y + y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, BLUE, rect)

        if current_step < len(visited_steps):

            x, y = visited_steps[current_step]

            rect = pygame.Rect(
                OFFSET_X + x * CELL_SIZE,
                OFFSET_Y + y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, YELLOW, rect)

        start_x = OFFSET_X
        start_y = OFFSET_Y

        start_rect = pygame.Rect(
            start_x,
            start_y,
            CELL_SIZE,
            CELL_SIZE
        )

        pygame.draw.rect(screen, GREEN, start_rect)

        s_text = self.font.render("S", True, BLACK)

        s_text_rect = s_text.get_rect(center=start_rect.center)

        screen.blit(s_text, s_text_rect)

        end_x = OFFSET_X + (self.cols - 1) * CELL_SIZE
        end_y = OFFSET_Y + (self.rows - 1) * CELL_SIZE

        end_rect = pygame.Rect(
            end_x,
            end_y,
            CELL_SIZE,
            CELL_SIZE
        )

        if goal_reached:
            pygame.draw.rect(screen, GREEN, end_rect)
        else:
            pygame.draw.rect(screen, (255, 100, 100), end_rect)

        e_text = self.font.render("E", True, BLACK)

        e_text_rect = e_text.get_rect(center=end_rect.center)

        screen.blit(e_text, e_text_rect)
