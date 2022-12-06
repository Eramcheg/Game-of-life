import pygame

class Cube:
    def __init__(self):
        pass


class Game:
    life=[]

    def __init__(self, cubes=0):

        for i in range(20):
            self.life.append([])
        # for i in range(20):
        #     for j in range(20):


    def drawGrid(self,w,rows,surface):
        size=w//rows
        x=0
        y=0
        for i in range(rows):
            x=x+size
            y=y+size
            pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
            pygame.draw.line(surface,(255,255,255),(0,y),(w,y))
        for i in range(20):
            pygame.draw.rect(surface,"white",(30*i,0,30,30))

    def redrawWindow(self, surface):
        surface.fill((0,0,0))
        self.drawGrid(width,rows,surface)
        pygame.display.update()

    def startGame(self):
        global width,rows
        width=600
        rows=20
        height=600
        win=pygame.display.set_mode((width,width))
        clock=pygame.time.Clock()

        flag=True
        while flag:
            pygame.time.delay(50)
            clock.tick(10)
            self.redrawWindow(win)

game=Game()
game.startGame()