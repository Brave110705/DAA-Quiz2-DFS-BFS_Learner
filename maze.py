import random
import pygame
from pathlib import Path

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (100, 100, 100)
BLUE = (80, 140, 255)
YELLOW = (255, 220, 100)
GREEN = (100, 255, 100)

CELL_SIZE = 50
OFFSET_X = 150
OFFSET_Y = 80
SOURCE_TILE_SIZE = 16
TILESET_PATH = Path(__file__).with_name("stone_to_void.png")

WALL_NORTH = 1
WALL_EAST = 2
WALL_SOUTH = 4
WALL_WEST = 8

# 4-bit wall-neighbor mask -> atlas tile coordinate, in 16 px cells.
# Tune these coordinates if you want a different tile from stone_to_void.png.
WALL_AUTOTILES = {
    0: (0, 0),
    WALL_NORTH: (4, 0),
    WALL_EAST: (2, 1),
    WALL_NORTH | WALL_EAST: (2, 0),
    WALL_SOUTH: (4, 2),
    WALL_NORTH | WALL_SOUTH: (4, 1),
    WALL_EAST | WALL_SOUTH: (2, 2),
    WALL_NORTH | WALL_EAST | WALL_SOUTH: (3, 1),
    WALL_WEST: (6, 1),
    WALL_NORTH | WALL_WEST: (6, 0),
    WALL_EAST | WALL_WEST: (5, 1),
    WALL_NORTH | WALL_EAST | WALL_WEST: (5, 0),
    WALL_SOUTH | WALL_WEST: (6, 2),
    WALL_NORTH | WALL_SOUTH | WALL_WEST: (5, 2),
    WALL_EAST | WALL_SOUTH | WALL_WEST: (3, 2),
    WALL_NORTH | WALL_EAST | WALL_SOUTH | WALL_WEST: (3, 0),
}

goal_reached = False

class Maze:

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        self.grid = []

        self.font = pygame.font.SysFont(None, 36)
        self.wall_tiles = self._load_wall_tiles()

        self.generate()

    def _load_wall_tiles(self):

        if not TILESET_PATH.exists():
            return {}

        tileset = pygame.image.load(str(TILESET_PATH))

        if pygame.display.get_surface():
            tileset = tileset.convert_alpha()
        tiles = {}

        for mask, atlas_position in WALL_AUTOTILES.items():
            atlas_x, atlas_y = atlas_position

            tile_rect = pygame.Rect(
                atlas_x * SOURCE_TILE_SIZE,
                atlas_y * SOURCE_TILE_SIZE,
                SOURCE_TILE_SIZE,
                SOURCE_TILE_SIZE
            )

            if not tileset.get_rect().contains(tile_rect):
                continue

            tile = tileset.subsurface(tile_rect).copy()
            tiles[mask] = pygame.transform.scale(tile, (CELL_SIZE, CELL_SIZE))

        return tiles

    def generate(self):

        self.grid = []

        for y in range(self.rows):

            row = []

            for x in range(self.cols):

                if (x == 0 and y == 0) or (
                    x == self.cols - 1 and y == self.rows - 1
                ):
                    row.append(0)

                else:
                    row.append(1 if random.random() < 0.25 else 0)

            self.grid.append(row)

    def is_walkable(self, x, y):

        return (
            0 <= x < self.cols
            and 0 <= y < self.rows
            and self.grid[y][x] == 0
        )

    def _is_wall(self, x, y):

        return (
            0 <= x < self.cols
            and 0 <= y < self.rows
            and self.grid[y][x] == 1
        )

    def _get_wall_mask(self, x, y):

        mask = 0

        if self._is_wall(x, y - 1):
            mask |= WALL_NORTH

        if self._is_wall(x + 1, y):
            mask |= WALL_EAST

        if self._is_wall(x, y + 1):
            mask |= WALL_SOUTH

        if self._is_wall(x - 1, y):
            mask |= WALL_WEST

        return mask

    def draw(self, screen, visited_steps, current_step, goal_reached):

        for y in range(self.rows):

            for x in range(self.cols):

                rect = pygame.Rect(
                    OFFSET_X + x * CELL_SIZE,
                    OFFSET_Y + y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )

                if self.grid[y][x] == 1:
                    wall_mask = self._get_wall_mask(x, y)
                    wall_tile = self.wall_tiles.get(wall_mask)

                    if wall_tile:
                        screen.blit(wall_tile, rect)
                    else:
                        pygame.draw.rect(screen, BLACK, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)

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
