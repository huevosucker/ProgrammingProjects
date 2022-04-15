

def setup():
    global img
    size(1000,1000)
def draw():
    imageMode(CENTER)
    bg = loadImage("board.png");
    image(bg,500,500,1000,1000)
    start = loadImage("snake.png");
    image(start,500,350,700,700);
