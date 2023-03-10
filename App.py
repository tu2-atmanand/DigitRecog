
import tkinter as tk
from tkinter.ttk import *
from prompt_toolkit.data_structures import Size
import win32gui
# import pywin
from PIL import ImageGrab, Image, ImageOps

import Test
class App(tk.Tk):
    # -----------------------FrontEnd GUI -------------------------
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=300, height=300, bg='white', cursor='cross')
        self.label = tk.Label(self, text="Draw a digit", font=("Helvetica", 48), foreground='lightgreen', background='black', width=8)
        self.label.grid(row=0, padx=2, pady=2)
        self.label = tk.Label(self, text=" RESULT ", font=("Helvetica", 48), foreground='lightgreen', background='black')
        self.canvas.grid(row=1, column=0, pady=2, padx=2)
        self.label.grid(row=1, column=1, pady=2, padx=2)

        # -----buttons------
        st = Style()
        st.configure('W.TButton', font=('calibri', 20, 'bold'), foreground='red', background='red')
        # self.clear_button = Button(self, text="Clear", style='W.TButton', width=20, command=self.clear).place(x=390, y=670)
        self.clear_button = Button(self, text="Clear", style='W.TButton', width=20, command=self.clear)
        self.clear_button.grid(row=2,column=0,pady=10,padx=30)

        # st.configure('W.TButton', font=('calibri', 10, 'bold'), foreground='green', background='green')
        # # self.clear_button = Button(self, text="Save", style='W.TButton', width=20, command=self.clear).place(x=50, y=670)
        # self.clear_button = Button(self, text="Save", style='W.TButton', width=20, command=self.clear)
        # self.clear_button.grid(row=2,column=0,pady=10,padx=10)
        # self.clear_button = tk.Button(self,text="Clear", command=self.clear,foreground='white',background='red',font=('calibri',10))

        self.classification_button = tk.Button(self, text="Classify", command=self.classify_handwriting, background='yellow', foreground='black')
        self.classification_button.grid(row=2, column=1, pady=2, padx=2)

        self.canvas.bind("<B1-Motion>", self.draw)

    # -----------------------BackEnd ---------------------------
    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        im = ImageGrab.grab(rect)
        im = im.convert("L")
        im = ImageOps.invert(im)
        im = im.convert("1")
        im = im.convert()
        digit, acc = Test.make_prediction(im)
        # print(digit)
        # print("  ")
        # print(acc)
        self.label.configure(text='---RESULT---\n\n\nDIGIT =  ' + str(digit) + '\n\n Accuracy = ' + str(int(acc * 100)) + "%", font=("Helvetica", 24))

        # comment out below two lines :
        # digit = 7
        # acc = 0.99


    def clear(self):
        self.canvas.delete("all")

    def draw(self, event):
        # try:
        #     print(event.x)
        #     print(Event.y)
        # except Exception as e:
        #     print(e)

        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill="black")


app = App()
tk.mainloop()
