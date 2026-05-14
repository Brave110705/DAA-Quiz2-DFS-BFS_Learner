import random
import pygame

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (100, 100, 100)
BLUE = (80, 140, 255)
YELLOW = (255, 220, 100)
GREEN = (100, 255, 100)

CELL_SIZE = 50
OFFSET_X = 150
OFFSET_Y = 80

goal_reached = False

class Maze:

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        self.grid = []

        self.font = pygame.font.SysFont(None, 36)

        self.generate()

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