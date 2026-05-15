import pygame

BLUE = (80, 140, 255)
RED = (255, 100, 100)
ORANGE = (230, 150, 60)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)

        self.bfs_button = pygame.Rect(80, 620, 140, 50)
        self.dfs_button = pygame.Rect(240, 620, 140, 50)
        self.dijkstra_button = pygame.Rect(400, 620, 140, 50)
        self.replay_button = pygame.Rect(560, 620, 140, 50)

    def _draw_button(self, screen, rect, color, label):

        pygame.draw.rect(screen, color, rect)
        text = self.font.render(label, True, WHITE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    def draw(self, screen, score, streak, message):

        self._draw_button(screen, self.bfs_button, BLUE, "BFS")
        self._draw_button(screen, self.dfs_button, RED, "DFS")
        self._draw_button(screen, self.dijkstra_button, ORANGE, "Dijkstra")
        self._draw_button(screen, self.replay_button, GREEN, "Replay")

        score_text = self.small_font.render(
            f"Score: {score}", True, BLACK
        )

        streak_text = self.small_font.render(
            f"Streak: {streak}", True, BLACK
        )

        screen.blit(score_text, (20, 20))
        screen.blit(streak_text, (20, 50))

        if message:

            result_text = self.font.render(message, True, BLACK)

            screen.blit(result_text, (250, 20))
