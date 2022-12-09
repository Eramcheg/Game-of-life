import tkinter as tk
from tkinter import ttk
import json


class SettingsC:
    def __init__(self):
        self.resolutionValues = list()
        self.resolutionValues.append(600)
        self.resolutionValues.append(800)
        self.resolutionValues.append(1000)

        self.rowsValues=list()
        self.rowsValues.append(10)
        self.rowsValues.append(20)
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
        frame.columnconfigure(3, weight=1)

        frame.pack(pady=200)

        label1 = tk.Label(frame, text="Life speed")
        textField = tk.Scale(frame, from_=80, to=1000, orient='horizontal')
        textField.set(data['speed'])
        label1.grid(row=0, column=0, sticky=tk.E + tk.W)
        textField.grid(row=0, column=1, sticky=tk.E + tk.W)



        label2 = tk.Label(frame, text="Window width")
        combobox2 = ttk.Combobox(frame, values=self.resolutionValues)
        combobox2.set(data['resolution'])


        if combobox2.get() == '600':
            self.rowsValues.append(30)
        elif combobox2.get() == '800':
            self.rowsValues.append(40)
        elif combobox2.get() == '1000':
            self.rowsValues.append(50)
        label3 = tk.Label(frame, text="Rows amount")
        combobox = ttk.Combobox(frame, values=self.rowsValues)

        combobox.set(data['rows'])
        label3.grid(row=2, column=0, sticky=tk.E + tk.W)
        combobox.grid(row=2, column=1, sticky=tk.E + tk.W)

        combobox2.bind('<<ComboboxSelected>>', lambda event, x=combobox: self.valueChanged(event,x))
        label2.grid(row=1, column=0, sticky=tk.E + tk.W)
        combobox2.grid(row=1, column=1, sticky=tk.E + tk.W)

        backBtn = tk.Button(frame, text="Back", font=('Arial', 18),
                            command=lambda: self.backMenu(root, int(textField.get()), int(combobox.get()),int(combobox2.get())))
        backBtn.grid(row=3, column=0, sticky=tk.E + tk.W)

        quitBtn = tk.Button(frame, text="Quit", font=('Arial', 18), command=self.quitSettings)
        quitBtn.grid(row=3, column=1, sticky=tk.E + tk.W)
        root.mainloop()

    def valueChanged(self,event,combobox):
        self.rowsValues.pop()
        if event.widget.get()=='600':
            self.rowsValues.append(30)
        elif event.widget.get()=='800':
            self.rowsValues.append(40)
        combobox.configure(values=self.rowsValues)
        combobox.set(self.rowsValues[0])
        combobox.update()

    def backMenu(self, root, speed, rows,resolution):
        root.destroy()
        file = open('settings.json')
        data = json.load(file)
        data["speed"] = speed
        data["rows"] = rows
        if resolution not in self.resolutionValues:
            data["resolution"]=self.resolutionValues[0]
        else:
            data["resolution"] = resolution
        with open("settings.json", "w") as outfile:
            outfile.write(json.dumps(data, indent=4))
        self.openMenu()

    def openMenu(self):
        from Menu import MenuClass
        menu = MenuClass()
        menu.startMenu()

    def quitSettings(self):
        exit()
