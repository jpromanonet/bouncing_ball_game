import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Create the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.randint(3, 5), random.randint(3, 5)]

# Create the platform
platform_pos = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_pos[0] > 0:
        platform_pos[0] -= 5
    if keys[pygame.K_RIGHT] and platform_pos[0] < WIDTH - PLATFORM_WIDTH:
        platform_pos[0] += 5

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Check if the ball hits the platform
    if (
        platform_pos[0] <= ball_pos[0] <= platform_pos[0] + PLATFORM_WIDTH
        and platform_pos[1] <= ball_pos[1] <= platform_pos[1] + PLATFORM_HEIGHT
    ):
        ball_speed[1] = -ball_speed[1]

    # Check if the ball falls off the screen
    if ball_pos[1] >= HEIGHT:
        # Reset the ball position
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        # Randomize the ball speed
        ball_speed = [random.randint(3, 5), random.randint(3, 5)]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Draw the platform
    pygame.draw.rect(screen, WHITE, (int(platform_pos[0]), int(platform_pos[1]), PLATFORM_WIDTH, PLATFORM_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
