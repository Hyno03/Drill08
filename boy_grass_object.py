from pico2d import *
import random

# Game object class here
class Grass():
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass
class smallBall():
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(10,790), 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y >= 69:
            self.y -= random.randint(1,20)

class bigBall():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(10, 790), 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y >= 79:
            self.y -= random.randint(1,20)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global balls

    running = True
    grass = Grass()
    balls = [smallBall() for i in range(10)] + [bigBall() for i in range(10)]
    pass

def update_world():
    grass.update()
    for ball in balls:
        ball.update()

def render_world():
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    pass

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
