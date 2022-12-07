import pygame

class Cube:
    def __init__(self):
        pass


class Game:
    life=[]
    rows=10
    Counter=0
    stopFlag=False
    def __init__(self, cubes=0):

        for i in range(self.rows):
            self.life.append([])
            for j in range(self.rows):
                self.life[i].append(0)



    def drawGrid(self,w,rows,surface):
        size=w//rows
        x=0
        y=0
        for i in range(rows):
            x=x+size
            y=y+size
            pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
            pygame.draw.line(surface,(255,255,255),(0,y),(w,y))


    def draw(self,surface,i):
        life=self.life
        #for cell_indexi in range(rows):
            #for cell_indexj in range(rows)
            #if cell==1:
                #pygame.draw.rect(surface, (255, 255, 255), (60, 60 * i, 60, 60))
        pygame.draw.rect(surface, (255, 255, 255), (60, 60*i, 60, 60))



    def redrawWindow(self, surface,i):
        surface.fill((0,0,0))
        self.drawGrid(width,rows,surface)
        self.draw(surface,i)
        pygame.display.update()

    def stopProgram(self,flagStop,Counter, win):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Counter += 1
                    if Counter % 2 is 0:
                        flagStop = False
                    else:
                        flagStop = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mx,my=pygame.mouse.get_pos()
                    pygame.draw.rect(win, (255, 255, 255), (mx//60 * 60, my//60 * 60, 60, 60))
                    pygame.display.update()
        return flagStop,Counter


    def startGame(self):
        global width,rows
        width=600                                  #Размер экрана игры
        rows=10                                    #Количество столбиков и рядков

        print(self.life)

        win=pygame.display.set_mode((width,width)) # Создание окна игры
        clock=pygame.time.Clock()                  #Запуск Игрового таймера
        flag=True
        i=0
        flagStop=False
        Counter=0
        while flag:
            pygame.time.delay(500)
            clock.tick(60)


            flagStop,Counter=self.stopProgram(flagStop,Counter,win)  #Пауза программы на пробел

            if flagStop is False:
                self.redrawWindow(win,i)
                i+=1

game=Game()
game.startGame()