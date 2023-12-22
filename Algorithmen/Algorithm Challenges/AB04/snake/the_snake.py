"""
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
"""

# setting up
import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
display = pygame.display.set_mode((800, 600))
display_background_color = (0, 102, 51)
clock = pygame.time.Clock()
pygame.display.set_caption("The Snake")
font = pygame.font.Font(None, 36)


class Snake:
    def __init__(self):
        self.position = [100, 100]
        self.body = [[100, 100]]
        self.size = (50, 15)
        self.color = (0, 0, 0)
        self.eye_color = (255, 255, 255)
        self.speed = 4
        self.direction = "RIGHT"
        self.score = 0

    def grow(self):
        if len(self.body) >= 2:
            tail, before_tail = self.body[-1], self.body[-2]
            new_segment = [tail[0] + (tail[0] - before_tail[0]), tail[1] + (tail[1] - before_tail[1])]
            self.body.append(new_segment)
        else:
            if self.direction == "RIGHT":
                self.body.append([self.body[-1][0] - self.size[0], self.body[-1][1]])
            elif self.direction == "LEFT":
                self.body.append([self.body[-1][0] + self.size[0], self.body[-1][1]])
            elif self.direction == "UP":
                self.body.append([self.body[-1][0], self.body[-1][1] + self.size[1]])
            elif self.direction == "DOWN":
                self.body.append([self.body[-1][0], self.body[-1][1] - self.size[1]])


class Rat:
    def __init__(self, rat_img):
        self.rat_img = rat_img
        self.rat_rect = self.rat_img.get_rect()
        self.spawn()

    def spawn(self):
        self.rat_rect.x = random.randint(0, screen_width - self.rat_rect.width)
        self.rat_rect.y = random.randint(0, screen_height - self.rat_rect.height)


big_rat_img = pygame.image.load("rat.png")
smaller_rat_img = pygame.transform.scale(big_rat_img, (45, 45))
snake = Snake()
rat = Rat(smaller_rat_img)

exit_ = False
# game loop
while not exit_:
    display.fill(display_background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_ = True
        # Handle key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and snake.direction != "RIGHT":
                snake.direction = "LEFT"
                snake.size = (50, 15)  # Snake horizontal
            elif event.key == pygame.K_d and snake.direction != "LEFT":
                snake.direction = "RIGHT"
                snake.size = (50, 15)  # Snake horizontal
            elif event.key == pygame.K_w and snake.direction != "DOWN":
                snake.direction = "UP"
                snake.size = (15, 50)  # Snake vertical
            elif event.key == pygame.K_s and snake.direction != "UP":
                snake.direction = "DOWN"
                snake.size = (15, 50)  # Snake vertical

    new_head = [snake.body[0][0], snake.body[0][1]]

    if snake.direction == "RIGHT":
        new_head[0] += snake.speed
    elif snake.direction == "LEFT":
        new_head[0] -= snake.speed
    elif snake.direction == "UP":
        new_head[1] -= snake.speed
    elif snake.direction == "DOWN":
        new_head[1] += snake.speed

    snake_head_rect = pygame.Rect(new_head[0], new_head[1], snake.size[0], snake.size[1])

    if snake_head_rect.colliderect(rat.rat_rect):
        rat.spawn()
        snake.score += 1
        snake.grow()
    else:
        snake.body.pop()

    snake.body.insert(0, new_head)
    score_text = font.render(f"Score: {snake.score}", True, (255, 255, 255))
    display.blit(score_text, (10, 10))

    # screen weapping
    head = snake.body[0]
    if head[0] >= screen_width:  # Off the right side
        head[0] = 0
    elif head[0] < 0:  # Off the left side
        head[0] = screen_width - snake.size[0]

    if head[1] >= screen_height:  # Off the bottom
        head[1] = 0
    elif head[1] < 0:  # Off the top
        head[1] = screen_height - snake.size[1]

    # Draw the snake
    for segment in snake.body:
        pygame.draw.rect(display, snake.color, pygame.Rect(segment[0], segment[1], snake.size[0], snake.size[1]),
                         border_radius=round(4))

    # Constants for the eye's position
    EYE_RADIUS = 3
    EYE_OFFSET = 7
    eye_x = head[0] + snake.size[0] // 2
    eye_y = head[1] + snake.size[1] // 2

    # Position the eye based on the direction
    if snake.direction == "RIGHT":
        eye_x = head[0] + snake.size[0] - EYE_OFFSET
        eye_y = head[1] + snake.size[1] // 2
    elif snake.direction == "LEFT":
        eye_x = head[0] + EYE_OFFSET
        eye_y = head[1] + snake.size[1] // 2
    elif snake.direction == "UP":
        eye_x = head[0] + snake.size[0] // 2
        eye_y = head[1] + EYE_OFFSET
    elif snake.direction == "DOWN":
        eye_x = head[0] + snake.size[0] // 2
        eye_y = head[1] + snake.size[1] - EYE_OFFSET

    # Draw the eye
    pygame.draw.circle(display, snake.eye_color, (eye_x, eye_y), EYE_RADIUS)
    display.blit(smaller_rat_img, rat.rat_rect)

    pygame.display.update()
    clock.tick(60)
