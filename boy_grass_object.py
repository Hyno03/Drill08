from pico2d import *

# Game object class here
class smallBall():
    def __init__(self):
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(100,100)

    def update(self):
        pass

class bigBall():
    def __init__(self):
        self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(200, 200)

    def update(self):
        pass

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
    global sb
    global bb

    running = True
    sb = smallBall()
    bb = bigBall()
    pass

def update_world():
    sb.update()
    bb.update()

def render_world():
    clear_canvas()
    sb.draw()
    bb.draw()
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
