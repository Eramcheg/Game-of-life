import pygame

class Cube:
    def __init__(self):
        pass


class Game:
    life=[]

    def __init__(self, cubes=0):

        for i in range(20):
            self.life.append([])


    def fucking_move(self,surface,i):
        pygame.draw.rect(surface, "white", (30 * i, 0, 30, 30))


    def drawGrid(self,w,rows,surface,i):
        size=w//rows
        x=0
        y=0
        for i in range(rows):
            x=x+size
            y=y+size
            pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
            pygame.draw.line(surface,(255,255,255),(0,y),(w,y))


    def draw(self,surface,i):
        pygame.draw.rect(surface, (255, 255, 255), (60, 60*i, 60, 60))
    def redrawWindow(self, surface,i):
        surface.fill((0,0,0))
        self.drawGrid(width,rows,surface,i)
        self.draw(surface,i)
        pygame.display.update()

    def startGame(self):
        global width,rows
        width=600
        rows=10
        win=pygame.display.set_mode((width,width))
        clock=pygame.time.Clock()

        flag=True
        i=0
        while flag:
            pygame.time.delay(500)
            clock.tick(60)

            self.redrawWindow(win,i)
            i+=1

game=Game()
game.startGame()