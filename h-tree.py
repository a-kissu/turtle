import turtle as tur
import random

def start(depth: int,
    length: float,
    speed: str='fastest'):

    tur.showturtle()
    tur.speed(speed)
    draw_tree(int(depth), length, 0.0, 0.0) # start from centre
    tur.done()

# def change_color():
    # colors = ["red", "blue", "green", "black", "yellow", "orange"]
    # tur.color(random.choice(colors))

def update_cors(x: float, y: float):
    tur.penup()
    tur.setpos(x, y)
    tur.pendown()

def rotate_n_draw(length: float, degree: int = 0):
    tur.right(degree)
    tur.forward(length)

def draw_tree(depth: int, length: float, x: float, y: float):
    update_cors(x, y)
    half = length / 2 # upper/lower part of the vertical line
        
    leftx = x - half
    rightx = x + half
    topy = y + half
    boty = y - half

    center = (topy + boty)/2

    # horizontal line
    update_cors(leftx, center)
    rotate_n_draw(length)

    # move to top left and draw vertical line
    update_cors(leftx, topy)
    rotate_n_draw(length, 90)


    # move to top right and draw vertical line
    update_cors(rightx, topy)
    rotate_n_draw(length)

    # start drawing from east side so turn toward that direction
    tur.left(90)

    # NOTE: i am supposed to use the value of root 2 to divide, but lines overlap when i do that so idk
    new_len = length / 2
    new_depth = depth - 1

    if new_depth > 0:
        draw_tree(new_depth, new_len, leftx, topy)
        draw_tree(new_depth, new_len, rightx, topy)
        draw_tree(new_depth, new_len, leftx, boty)
        draw_tree(new_depth, new_len, rightx, boty)

start(6, 500)
