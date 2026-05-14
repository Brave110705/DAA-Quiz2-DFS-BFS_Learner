import pygame
import random

from maze import Maze
from solver import Solver
from ui import UI

WIDTH = 800
HEIGHT = 700
FPS = 60

ROWS = 10
COLS = 10

BACKGROUND = (220, 220, 220)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BFS / DFS Learner")

clock = pygame.time.Clock()

maze = Maze(ROWS, COLS)
ui = UI()

visited_steps = []

current_step = 0

animation_delay = 250
animation_timer = 0

algorithm_used = ""

score = 0
streak = 0

message = ""

def start_round():

    global maze
    global visited_steps
    global current_step
    global animation_timer
    global algorithm_used
    global message

    message = ""

    maze.generate()

    start = (0, 0)
    goal = (COLS - 1, ROWS - 1)

    algorithm_used = random.choice(["BFS", "DFS"])

    if algorithm_used == "BFS":
        visited_steps = Solver.bfs(maze, start, goal)
    else:
        visited_steps = Solver.dfs(maze, start, goal)

    current_step = 0

    animation_timer = pygame.time.get_ticks()


def check_answer(answer):

    global score
    global streak
    global message

    if answer == algorithm_used:

        streak += 1

        score += 100 + (streak * 20)

        message = "Correct!"

    else:

        streak = 0

        message = f"Wrong! It was {algorithm_used}"

    start_round()

start_round()

running = True

while running:

    dt = clock.tick(FPS)

    screen.fill(BACKGROUND)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            if ui.bfs_button.collidepoint(mouse_pos):
                check_answer("BFS")

            if ui.dfs_button.collidepoint(mouse_pos):
                check_answer("DFS")

            if ui.replay_button.collidepoint(mouse_pos):

                current_step = 0
                animation_timer = pygame.time.get_ticks()

    now = pygame.time.get_ticks()

    if now - animation_timer > animation_delay:

        if current_step < len(visited_steps) - 1:
            current_step += 1

        animation_timer = now

    goal_position = (COLS - 1, ROWS - 1)

    goal_reached = (
        current_step < len(visited_steps)
        and visited_steps[current_step] == goal_position
    )

    maze.draw(
        screen,
        visited_steps,
         current_step,
        goal_reached
    )

    ui.draw(screen, score, streak, message)

    pygame.display.flip()

pygame.quit()