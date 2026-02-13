import pygame
import random
import sys
import math  

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock & font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Draw snake body
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Score display
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

# Game Over screen
def show_game_over(score):
    message = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(message, [WIDTH // 3.5, HEIGHT // 2])
    pygame.display.update()
    pygame.time.delay(2000)

# NEW: Draw animated food
def draw_food(x, y, frame_count):
    # Use sine wave to animate food size
    pulse = 4 * math.sin(frame_count * 0.2)  # Wobble effect
    size = BLOCK_SIZE + pulse
    offset = (BLOCK_SIZE - size) / 2  # Center the pulse
    pygame.draw.rect(screen, RED, (x + offset, y + offset, size, size))

# Game loop
def main():
    head_x = WIDTH // 2
    head_y = HEIGHT // 2
    vel_x = 0
    vel_y = 0

    snake = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    frame_count = 0  # 🌀 used for animating food

    running = True
    while running:
        screen.fill(BLACK)
        frame_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and vel_x == 0:
                    vel_x = -BLOCK_SIZE
                    vel_y = 0
                elif event.key == pygame.K_RIGHT and vel_x == 0:
                    vel_x = BLOCK_SIZE
                    vel_y = 0
                elif event.key == pygame.K_UP and vel_y == 0:
                    vel_y = -BLOCK_SIZE
                    vel_x = 0
                elif event.key == pygame.K_DOWN and vel_y == 0:
                    vel_y = BLOCK_SIZE
                    vel_x = 0

        head_x += vel_x
        head_y += vel_y
        head = [head_x, head_y]
        snake.append(head)

        if len(snake) > snake_length:
            del snake[0]

        # Collision checks
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or head in snake[:-1]:
            show_game_over(snake_length - 1)
            return

        # Eat food
        if head_x == food_x and head_y == food_y:
            snake_length += 1
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

        # Draw game elements
        draw_snake(snake)
        draw_food(food_x, food_y, frame_count)
        display_score(snake_length - 1)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    sys.exit()

# Run the game
main()
