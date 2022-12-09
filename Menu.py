import tkinter as tk
import GameClass
from tkinter import *

import Rules
import Settings


class MenuClass:

    def startMenu(self):
        root = tk.Tk()
        root.geometry("600x600")
        root.title("Menu")
        root.configure(background="black")

        buttonFrame = tk.Frame(root)
        buttonFrame.columnconfigure(0, weight=1)
        buttonFrame.columnconfigure(1, weight=1)
        buttonFrame.columnconfigure(2, weight=1)
        buttonFrame.columnconfigure(3,weight=1)

        buttonFrame.pack(pady=200)
        startGameBtn = tk.Button(buttonFrame, text="Start Game", font=('Arial', 18),
                                 command=lambda: self.startGame(root))
        startGameBtn.grid(row=0, column=1, sticky=tk.E + tk.W)

        settingsBtn = Button(buttonFrame, text="Settings", font=('Arial', 18),
                             command=lambda: self.startSettings(root))
        settingsBtn.grid(row=1, column=1, sticky=tk.E + tk.W)

        rulesBtn=Button(buttonFrame,text="Rules",font=('Arial',18), command=lambda:self.startRules(root))
        rulesBtn.grid(row=2,column=1,sticky=tk.E+tk.W)

        quitBtn = tk.Button(buttonFrame, text="Quit", font=('Arial', 18), command=self.quitMenu)
        quitBtn.grid(row=3, column=1, sticky=tk.E + tk.W)



        root.mainloop()

    def startGame(self, root):
        root.destroy()
        self.openGame()

    def openGame(self):
        game = GameClass.Game()
        game.startGame()

    def startSettings(self, root):
        root.destroy()
        self.openSettings()

    def openSettings(self):
        settings = Settings.SettingsC()
        settings.windowSettings()

    def startRules(self,root):
        root.destroy()
        self.openRules()

    def openRules(self):
        rules=Rules.RulesClass()
        rules.startRules()

    def quitMenu(self):
        exit()


st = MenuClass()
st.startMenu()
