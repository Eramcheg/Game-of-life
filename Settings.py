import sys
import tkinter as tk


class SettingsC:

    def windowSettings(self):
        root = tk.Tk()
        root.geometry("600x600")
        root.title("Settings")
        root.configure(background="black")

        frame = tk.Frame(root)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        frame.pack(pady=200)

        label1=tk.Label(frame,text="Setting 1")
        textField=tk.Text(frame, font=('Arial',14), height=1,width=10)
        label1.grid(row=0,column=0, sticky=tk.E+tk.W)
        textField.grid(row=0, column=1, sticky=tk.E + tk.W)

        backBtn=tk.Button(frame,text="Back",font=('Arial',18),command=lambda:self.backMenu(root))
        backBtn.grid(row=2,column=0,sticky=tk.E + tk.W)

        quitBtn = tk.Button(frame, text="Quit", font=('Arial', 18), command=self.quitSettings)
        quitBtn.grid(row=2, column=1, sticky=tk.E + tk.W)
        root.mainloop()

    def backMenu(self,root):
        root.destroy()
        self.openMenu()

    def openMenu(self):
        from Menu import Menu
        menu = Menu()
        menu.startMenu()
    def quitSettings(self):
       exit()
