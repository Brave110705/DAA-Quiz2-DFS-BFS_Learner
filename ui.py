import pygame

BLUE = (80, 140, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)

class UI:

    def __init__(self):

        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)

        self.bfs_button = pygame.Rect(150, 620, 150, 50)
        self.dfs_button = pygame.Rect(325, 620, 150, 50)
        self.replay_button = pygame.Rect(500, 620, 150, 50)

    def draw(self, screen, score, streak, message):

        pygame.draw.rect(screen, BLUE, self.bfs_button)
        pygame.draw.rect(screen, RED, self.dfs_button)
        pygame.draw.rect(screen, GREEN, self.replay_button)

        bfs_text = self.font.render("BFS", True, WHITE)
        dfs_text = self.font.render("DFS", True, WHITE)
        replay_text = self.font.render("Replay", True, WHITE)

        screen.blit(bfs_text, (195, 632))
        screen.blit(dfs_text, (370, 632))
        screen.blit(replay_text, (535, 632))

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