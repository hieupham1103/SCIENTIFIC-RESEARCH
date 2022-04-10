import random

countRec = 0
countCir = 0
centerX = 500
centerY = 400
R = 200
maxCount = 10

def setup():
    
    background(255, 255, 255)
    size(800, 800)
    # fill(255, 255, 255)
    strokeWeight(2)
    rect(300, 200, 400, 400)
    fill(255, 255, 255)
    circle(centerX, centerY, R * 2)
    fill(0, 0, 0)
    circle(centerX, centerY, 10)
    delay(3000)
    
    
    
def draw():
    # strokeWeight(1)
    noStroke()

    font = createFont("monospaced", 16, True)
    count = 0
    while(count < maxCount):
        count += 1
        x = random.randint(300,700)
        y = random.randint(200,600)
        fill(255, 255, 255)
        rect(5, 120, 280, 550)
        fill(0, 0, 0)
        textFont(font,30)
        text("In Rec",10,150)
        text("In Cir",10,250)
    
        dis = (centerX - x)**2 + (centerY - y)**2
        check = 0
    
        if dis <= R * R:
            fill(255,0,0)
            circle(x, y, 4)
            check = 1
        else:
            fill(15, 3, 252)
            circle(x, y, 4)
        
        global countRec
        countRec += 1
        global countCir
        countCir += check 
        
        fill(80, 80, 80)
        text(countRec, 10, 200)
        text(countCir, 10, 300)
        
        fill(0, 0, 0)
        text("Dot",10,600)
        fill(80, 80, 80)
        text(x,10,650)
        text(y,100,650)
        
    fill(0, 0, 0)
    text("PI",10,350)
    
    pi = 4.0 * countCir / countRec
    text(str(PI),10,400)
    fill(80, 80, 80)
    text(str(pi),10,450)
    fill(0, 0, 0)
    text("Diff",10,500)
    fill(80, 80, 80)
    text(str(abs(PI - pi) / PI * 100)[0:4] + "%",10,550)
    
    
    print(pi)
    
    delay(1)


    
