import sys
import pygame
pygame.init()
class Game:
    life=[]                  #Объявление глобальных переменных
    rows=20
    Counter=0
    speed=150
    width=600
    CubeSize=width//rows
    stopFlag=False



    def __init__(self):

        for i in range(self.rows):          #Заполнение примитивного массива игры мертвыми клетками
            self.life.append([])
            for j in range(self.rows):
                self.life[i].append(0)




    def drawGrid(self,w,rows,surface):         #Прорисовка сетки поля
        size=w//rows
        x=0
        y=0
        for i in range(rows):
            x=x+size
            y=y+size
            pygame.draw.line(surface,(200,200,200),(x,0),(x,w))
            pygame.draw.line(surface,(200,200,200),(0,y),(w,y))



    # Рабочий алгоритм игры "Жизнь", продемонстрированный в файле Primitive.py
    def algorithm(self):
        life=self.life
        life_kopie=[]
        Length=len(life)
        for i in range(Length):
            life_kopie.append([])
        for i in range(Length):
            for j in range(Length):
                life_kopie[i].append(life[i][j])

        for i in range(Length):
            for j in range(Length):
                zivot = 0
                for o in range(-1, 2):
                    for k in range(-1, 2):
                        first = (i + o)
                        second = (j + k)
                        if first != -1:
                            first = first % Length
                        if second != -1:
                            second = second % Length
                        if life[first][second] == 1 and (first != i or second != j):
                            zivot += 1
                if zivot < 2:
                    life_kopie[i][j] = 0
                elif zivot == 2:
                    if (life_kopie[i][j] != 0):
                        life_kopie[i][j] = 1
                elif zivot == 3:
                    life_kopie[i][j] = 1
                else:
                    life_kopie[i][j] = 0
        self.life=life_kopie




    def draw(self,surface):
        life=self.life
        Length=len(life)
        for i in range(Length):
            for j in range(Length):
                if life[i][j]==1:
                    pygame.draw.rect(surface, (255, 255, 255), (j *self.CubeSize, i * self.CubeSize, self.CubeSize, self.CubeSize))
                    #Проверяем какие клетки у нас живые
                    #после чего закрашиваем их



    # Обновление картинки на экране
    def redrawWindow(self, surface):
        surface.fill((0,0,0))
        self.drawGrid(width,rows,surface)
        self.draw(surface)
        self.algorithm()
        pygame.display.update()



    # Пауза программы и возможности во время паузы
    def pauseProgram(self,flagStop,Counter, win):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                #Проверка на нажатие кнопки паузы
                    Counter += 1
                    if Counter % 2 != 0:
                        flagStop = False
                    else:
                        flagStop = True
                if event.key ==pygame.K_ESCAPE:                #Проверка на нажатие кнопки выхода
                    pygame.quit()
                    exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mx,my=pygame.mouse.get_pos()               #Считываем позицию курсора

                    x_coordinate=mx//self.CubeSize   #Координата х клетки
                    y_coordinate=my//self.CubeSize   #Координата у клетки


                    if self.life[y_coordinate][x_coordinate]!=1:
                        self.user_drawing(win,(255,255,255),x_coordinate,y_coordinate,1)  #Если клетка мертва и мы кликаем
                                                                                          #То превращаем клетку в живую
                    else:
                        self.user_drawing(win,(0,0,0),x_coordinate,y_coordinate,0)        #Если клетка жива и мы кликаем
                                                                                          #То превращаем клетку в мертвую

                    pygame.display.update()
        return flagStop,Counter



    #Процесс создания клетки пользователем во время паузы
    def user_drawing(self,surface, color, x_coordinate,y_coordinate, cell_type):
        pygame.draw.rect(surface, color, (x_coordinate * self.CubeSize, y_coordinate * self.CubeSize, self.CubeSize, self.CubeSize))
        self.life[y_coordinate][x_coordinate] = cell_type
        pygame.draw.line(surface, (200, 200, 200), (x_coordinate * self.CubeSize, 0), (x_coordinate * self.CubeSize, self.width))
        pygame.draw.line(surface, (200, 200, 200), (0, y_coordinate * self.CubeSize), (self.width, y_coordinate * self.CubeSize))



    #Ядро программы создающее окно и его настройку
    def startGame(self):
        global width,rows
        width=self.width           #Размер экрана игры
        rows=self.rows             #Количество столбиков и рядков


        win=pygame.display.set_mode((width,width)) # Создание окна игры
        #win.display.set_caption("New")
        pygame.display.set_caption("Gane of life")
        clock=pygame.time.Clock()                  #Запуск Игрового таймера
        flag=True
        i=0
        flagStop=True
        Counter=0

        self.redrawWindow(win)
        while flag:
            pygame.time.delay(self.speed)
            clock.tick(60)
            flagStop,Counter=self.pauseProgram(flagStop,Counter,win)  #Пауза программы на пробел
            if flagStop is False:
                self.redrawWindow(win)
                i+=1
                pygame.display.set_caption("Game of life")
            else:
                pygame.display.set_caption("Game is paused, draw something")

#
# game=Game()
# game.startGame()