# ochki = 0
# a = 30
# b = 200
# timer = 5
# maxim = 60
# def CollideTC(x,y,x1,x2,d):
#     if dist(x,y,x1,x2) <= d/2:
#         return True
#     else:
#         return False
# def CollideBC(xb,yb,x1b,x2b,db):
#     if dist(xb,yb,x1b,x2b) <= db/2:
#         return True
#     else:
#         return False
# def setup():
#     size(1000,1000)
#     background(1)
#     textSize(23)
# def draw():
#     global maxim,timer,a,b,ochki
#     background(1)
#     ellipse(500,500,50,50)
#     ellipse(a,b,10,10)
#     rect(800,900,200,100)
#     fill(1)
#     text("Perezagruzka",820,960)
#     fill(255)
#     text("ochki",850,100)
#     text(ochki, 930,100)
#     if ochki >= 1000:
#         noLoop()
#         background(1)
#         textSize(50)
#         text(u"Победа", 400, 500)
#     elif timer > 0:
#         text(timer, 100, 100)
#         maxim = maxim - 1
#         if maxim == 0:
#             maxim = 60
#             timer -= 1
#     if timer == 0:
#         noLoop()
#         background(1)
#         textSize(50)
#         text(u"Проигрыш", 400, 500)
#     if keyPressed == True:
#         if key == 'p' or key == 'P' or key == 'з' or key == 'З':
#             noLoop()
#     if mousePressed == True:
#         if mouseX > 800 and mouseX < 1000 and mouseY > 900 and mouseY < 1000:
#             timer = 5
#             ochki = 0
# def mouseClicked():
#     global ochki,timer,a,b
#     if CollideTC(mouseX,mouseY,500,500,50):
#         ochki += 10
#     if CollideBC(mouseX,mouseY,a,b,10):
#         timer += 3
#         a = random(1,1000)
#         b = random(1,1000)
# def keyReleased():
#     loop()
def CollideCR(x,y,w,f,x1,y1,d):
    testX = 0
    testY = 0
    if x1 < x:
        testX = x
    elif x1 > x + w:
        testX = x + w
    if y1 < y:
        testY = y
    elif y1 > y + f:
        testY = y + f
    distan = dist(x1,y1,testX,testY)
    if distan <= d/2:
        return True
    else:
        return False
a = 25
b = 25
def setup():
    size(1000,1000)
    background(1)
def draw():
    global a,b
    background(1)
    if CollideCR(300,800,400,850,a,b,50):
        loop()
        background(1)
    else:
        rect(300,800,100,50)
        ellipse(a,b,50,50)
    if keyPressed == True:
        if key == CODED:
            if keyCode == UP:
                b -= 5
            if keyCode == DOWN:
                b += 5
            if keyCode == LEFT:
                a -= 5
            if keyCode == RIGHT:
                a += 5  
