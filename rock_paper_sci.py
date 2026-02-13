import pygame
import random
import sys

# Setup
pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Game options
choices = ["Rock", "Paper", "Scissors"]

# Button data
buttons = {
    "Rock": pygame.Rect(50, 250, 100, 50),
    "Paper": pygame.Rect(200, 250, 100, 50),
    "Scissors": pygame.Rect(350, 250, 100, 50)
}

# Game state
player_choice = ""
computer_choice = ""
result = ""

# Result logic
def get_result(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Title
    title = font.render("Choose your move:", True, BLACK)
    screen.blit(title, (150, 30))

    # Draw buttons
    for name, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        text = font.render(name, True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 10))

    # Show choices and result
    if player_choice:
        pc_text = font.render(f"You chose: {player_choice}", True, DARK_GRAY)
        cc_text = font.render(f"Computer chose: {computer_choice}", True, DARK_GRAY)
        result_text = font.render(result, True, BLACK)
        screen.blit(pc_text, (100, 100))
        screen.blit(cc_text, (100, 140))
        screen.blit(result_text, (100, 180))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    player_choice = name
                    computer_choice = random.choice(choices)
                    result = get_result(player_choice, computer_choice)

    pygame.display.flip()

pygame.quit()
sys.exit()
