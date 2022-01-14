import random

def setup():
    size(800, 800)
    fill(15, 3, 252)
    rect(300, 200, 400, 400)
    fill(3, 152, 252)
    circle(500, 400, 400)
    
def draw():
    x = random.randint(300,700)
    y = random.randint(200,600)
    circle(x, y, 1)
    fill(0, 0, 0)
    rect(0, 0, 300, 300)
    font = createFont("Arial", 16, True)
    fill(255, 255, 255)
    textFont(font,30)
    
    text(x,10,100)
    text(y,100,100)

    
