import tkinter as tk
import PauseMenu
import threading
from tkinter import *
class Menu:
     root = tk.Tk()
     def startMenu(self):
        root=self.root
        root.geometry("600x600")
        root.title("Menu")
        root.configure(background="black")

        buttonFrame=tk.Frame(root)
        buttonFrame.columnconfigure(0,weight=1)
        buttonFrame.columnconfigure(1, weight=1)
        buttonFrame.columnconfigure(2, weight=1)

        buttonFrame.pack(pady=200)
        startGameBtn=tk.Button(buttonFrame,text="Start Game",font=('Arial',18),command=self.startGame)
        startGameBtn.grid(row=0,column=1, sticky=tk.E+tk.W)

        settingsBtn = Button(buttonFrame, text="Settings", font=('Arial', 18))
        settingsBtn.grid(row=2,column=1,sticky=tk.E+tk.W)

        quitBtn=tk.Button(buttonFrame,text="Quit",font=('Arial', 18),command= self.quitMenu)
        quitBtn.grid(row=3,column=1,sticky=tk.E+tk.W)

        root.mainloop()

     def startGame(self):
        self.root.destroy()
        t1=threading.Thread(target=self.openGame)
        t1.start()
        t1.join()

     def openGame(self):
        game = PauseMenu.Game()
        game.startGame()

     def quitMenu(self):
        exit()
     #   exit()
st=Menu()
st.startMenu()

