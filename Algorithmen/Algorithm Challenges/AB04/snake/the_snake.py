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

# my code
"""
# setting up
import pygame
import random
from tkinter import *
from tkinter import messagebox

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
        self.turns = {}

    def grow(self):
        tail = self.body[-1]
        if self.direction == "RIGHT":
            self.body.append([tail[0] - self.size[0], tail[1]])
        elif self.direction == "LEFT":
            self.body.append([tail[0] + self.size[0], tail[1]])
        elif self.direction == "UP":
            self.body.append([tail[0], tail[1] - self.size[1]])
        elif self.direction == "DOWN":
            self.body.append([tail[0], tail[1] + self.size[1]])

    def add_turn(self, point):
        self.turns[point] = self.direction

    def update_body(self):
        for i, segment in enumerate(self.body):
            p = tuple(segment)
            if p in self.turns:
                turn_direction = self.turns[p]
                # Update direction if we are at a turn point
                self.direction = turn_direction
                # Remove the turn point if it's the last segment
                if i == len(self.body) - 1:
                    del self.turns[p]

        # Move each segment
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1][:]

        # Move the head
        if self.direction == "RIGHT":
            self.body[0][0] += self.speed
        elif self.direction == "LEFT":
            self.body[0][0] -= self.speed
        elif self.direction == "UP":
            self.body[0][1] -= self.speed
        elif self.direction == "DOWN":
            self.body[0][1] += self.speed


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

        # Update the head's position
        snake.position[
            0] += snake.speed if snake.direction == "RIGHT" else -snake.speed if snake.direction == "LEFT" else 0
        snake.position[
            1] += snake.speed if snake.direction == "DOWN" else -snake.speed if snake.direction == "UP" else 0

        # Record the point of turn
        if snake.direction in ["RIGHT", "LEFT"]:
            snake.add_turn((snake.position[0], snake.position[1]))
        elif snake.direction in ["UP", "DOWN"]:
            snake.add_turn((snake.position[0], snake.position[1]))

        # Now update the whole snake body
        snake.update_body()

        # Handle key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and snake.direction != "RIGHT":
                snake.direction = "LEFT"
                snake.size = (50, 15)  # Snake vertical
            elif event.key == pygame.K_d and snake.direction != "LEFT":
                snake.direction = "RIGHT"
                snake.size = (50, 15)  # Snake horizontal
            elif event.key == pygame.K_w and snake.direction != "DOWN":
                snake.direction = "UP"
                snake.size = (15, 50)  # Snake vertical
            elif event.key == pygame.K_s and snake.direction != "UP":
                snake.direction = "DOWN"
                snake.size = (15, 50)  # Snake horizontal

    new_head = [snake.body[0][0], snake.body[0][1]]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and snake.direction != "RIGHT":
        snake.direction = "LEFT"
        snake.size = (50, 15)  # Snake horizontal
        snake.add_turn(tuple(snake.body[0]))
    elif keys[pygame.K_d] and snake.direction != "LEFT":
        snake.direction = "RIGHT"
        snake.size = (50, 15)  # Snake horizontal
        snake.add_turn(tuple(snake.body[0]))
    elif keys[pygame.K_w] and snake.direction != "DOWN":
        snake.direction = "UP"
        snake.size = (15, 50)  # Snake vertical
        snake.add_turn(tuple(snake.body[0]))
    elif keys[pygame.K_s] and snake.direction != "UP":
        snake.direction = "DOWN"
        snake.size = (15, 50)  # Snake vertical
        snake.add_turn(tuple(snake.body[0]))

    # Update the snake's body each frame
    snake.update_body()

    snake_head_rect = pygame.Rect(snake.body[0][0], snake.body[0][1], snake.size[0], snake.size[1])
    if snake_head_rect.colliderect(rat.rat_rect):
        rat.spawn()
        snake.score += 1
        snake.grow()

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
    clock.tick(60)"""

# from internet
# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 102, 51)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 0, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('The Snake')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 5 seconds we will quit the program
    time.sleep(5)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 1
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
