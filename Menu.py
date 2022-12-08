import tkinter as tk
import GameClass
import threading
from tkinter import *
import Settings


class Menu:

     def startMenu(self):
        root = tk.Tk()
        root.geometry("600x600")
        root.title("Menu")
        root.configure(background="black")

        buttonFrame=tk.Frame(root)
        buttonFrame.columnconfigure(0,weight=1)
        buttonFrame.columnconfigure(1, weight=1)
        buttonFrame.columnconfigure(2, weight=1)

        buttonFrame.pack(pady=200)
        startGameBtn=tk.Button(buttonFrame,text="Start Game",font=('Arial',18),command= lambda: self.startGame(root))
        startGameBtn.grid(row=0,column=1, sticky=tk.E+tk.W)

        settingsBtn = Button(buttonFrame, text="Settings", font=('Arial', 18),command=lambda : self.SettingsMethod(root))
        settingsBtn.grid(row=2,column=1,sticky=tk.E+tk.W)

        quitBtn=tk.Button(buttonFrame,text="Quit",font=('Arial', 18),command= self.quitMenu)
        quitBtn.grid(row=3,column=1,sticky=tk.E+tk.W)

        root.mainloop()

     def startGame(self,root):
        root.destroy()
        self.openGame()

     def openGame(self):
        game = GameClass.Game()
        game.startGame()

     def SettingsMethod(self,root):
         root.destroy()
         self.openSettings()

     def openSettings(self):

         settin=Settings.SettingsC()
         settin.windowSettings()
     def quitMenu(self):
        exit()


st=Menu()
st.startMenu()

