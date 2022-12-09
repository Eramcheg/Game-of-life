import tkinter as tk

class RulesClass:
    def startRules(self):
        root = tk.Tk()
        root.geometry("600x600")
        root.title("Rules")
        root.configure(background="black")

        frame = tk.Frame(root)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        frame.pack(pady=50)
        Title1=tk.Label(frame,text="Main Rules",font=('Arial',18), justify='left')
        Title1.grid(row=1,column=2)

        Rules =tk.Label(frame,text="""1. Any live cell with fewer than two live neighbours dies, as if by\nunderpopulation. \n2. Any live cell with two or three live neighbours lives on\nto the next generation. \n3. Any live cell with more than three live neighbours dies, as if by\noverpopulation. \n4. Any dead cell with exactly three live neighbours becomes\na live cell, as if by reproduction""",font=('Arial',15), justify='left')
        Rules.grid(row=2,column=2)

        Title2=tk.Label(frame,text="\nInGame hotkeys",font=('Arial',18), justify='left')
        Title2.grid(row=3, column=2)

        HotKeys=tk.Label(frame,text="Q - Quit the game\nEscape - Back to main menu\nSpace - pause/resume game\n",font=('Arial',15), anchor="e",justify="left")
        HotKeys.grid(row=4,column=2)

        backBtn = tk.Button(frame, text="Back to Menu", font=('Arial', 18), command= lambda: self.backMenu(root))
        backBtn.configure(background='gray')
        backBtn.grid(row=5, column=2, sticky=tk.E + tk.W)

        root.mainloop()
        print("Rules")

    def backMenu(self,root):
        root.destroy()
        self.openMenu()

    def openMenu(self):
        from Menu import MenuClass
        menu = MenuClass()
        menu.startMenu()
