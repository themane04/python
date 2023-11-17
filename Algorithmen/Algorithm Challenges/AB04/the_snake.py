
def snake_function(side_length):
    snake_size = 1
    eating_tracker = -1
    total_blocks = side_length * side_length

    while snake_size <= total_blocks:
        snake_size *= 2
        eating_tracker += 1
    return eating_tracker


the_snake = snake_function(24)
print(the_snake)


"""# setting up
import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
display_background_color = (0, 102, 51)
clock = pygame.time.Clock()
pygame.display.set_caption("The Snake")

# snake properties
snake_pos = [100, 100]
snake_size = (50, 20)
snake_color = (0, 0, 0)
snake_eye_color = (255, 255, 255)
snake_speed = 5
direction = "RIGHT"

exit_ = False
# game loop
while not exit_:
    display.fill(display_background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True
        # Handle key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and direction != "RIGHT":
                direction = "LEFT"
                snake_size = (50, 20)  # Snake vertical
            elif event.key == pygame.K_d and direction != "LEFT":
                direction = "RIGHT"
                snake_size = (50, 20)  # Snake horizontal
            elif event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
                snake_size = (20, 50)  # Snake vertical
            elif event.key == pygame.K_s and direction != "UP":
                direction = "DOWN"
                snake_size = (20, 50)  # Snake horizontal

    # Update snake position
    if direction == "RIGHT":
        snake_pos[0] += snake_speed
    elif direction == "LEFT":
        snake_pos[0] -= snake_speed
    elif direction == "UP":
        snake_pos[1] -= snake_speed
    elif direction == "DOWN":
        snake_pos[1] += snake_speed

    # Draw the snake
    pygame.draw.rect(display, snake_color, pygame.Rect(snake_pos[0], snake_pos[1], snake_size[0], snake_size[1]),
                     border_radius=round(5))

    # Constants for the eye's position
    EYE_RADIUS = 5
    EYE_OFFSET = 20

    # Position the eye based on the direction
    if direction == "RIGHT":
        eye_x = snake_pos[0] + snake_size[0] - EYE_OFFSET
        eye_y = snake_pos[1] + snake_size[1] // 2
    elif direction == "LEFT":
        eye_x = snake_pos[0] + EYE_OFFSET
        eye_y = snake_pos[1] + snake_size[1] // 2
    elif direction == "UP":
        eye_x = snake_pos[0] + snake_size[0] // 2
        eye_y = snake_pos[1] + EYE_OFFSET
    elif direction == "DOWN":
        eye_x = snake_pos[0] + snake_size[0] // 2
        eye_y = snake_pos[1] + snake_size[1] - EYE_OFFSET

    eye_x = snake_pos[0] + snake_size[0] / 2
    eye_y = snake_pos[1] + snake_size[1] / 2

    # Draw the eye
    pygame.draw.circle(display, snake_eye_color, (eye_x, eye_y), EYE_RADIUS)

    pygame.display.update()
    clock.tick(60)"""
