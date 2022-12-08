import sys
import tkinter as tk
from tkinter import ttk
import json
class SettingsC:

    def windowSettings(self):
        file = open('settings.json')
        data = json.load(file)

        root = tk.Tk()
        root.geometry("600x600")
        root.title("Settings")
        root.configure(background="black")

        frame = tk.Frame(root)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        frame.pack(pady=200)

        label1=tk.Label(frame,text="Life speed")
        textField=tk.Scale(frame, from_= 80,to=1000,orient='horizontal')
        textField.set(data['speed'])
        label1.grid(row=0,column=0, sticky=tk.E+tk.W)
        textField.grid(row=0, column=1, sticky=tk.E + tk.W)


        k = []
        k.append(10)
        k.append(20)
        k.append(30)


        label2=tk.Label(frame,text="Rows amount")
        combobox=ttk.Combobox(frame,values=k)
        combobox.set(data['rows'])
        label2.grid(row=1,column=0, sticky=tk.E+tk.W)
        combobox.grid(row=1,column=1,sticky=tk.E+tk.W)



        backBtn=tk.Button(frame,text="Back",font=('Arial',18),command=lambda:self.backMenu(root, int(textField.get()),int(combobox.get())))
        backBtn.grid(row=2,column=0,sticky=tk.E + tk.W)

        quitBtn = tk.Button(frame, text="Quit", font=('Arial', 18), command=self.quitSettings)
        quitBtn.grid(row=2, column=1, sticky=tk.E + tk.W)
        root.mainloop()

    def backMenu(self,root,speed,rows):
        root.destroy()
        file = open('settings.json')
        data = json.load(file)
        data["speed"] = speed
        data["rows"]=rows
        with open("settings.json", "w") as outfile:
            outfile.write(json.dumps(data, indent=4))
        self.openMenu()


    def openMenu(self):
        from Menu import Menu
        menu = Menu()
        menu.startMenu()
    def quitSettings(self):
       exit()
