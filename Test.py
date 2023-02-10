
from keras.models import load_model
import numpy as np



model = load_model('modell.h5')
def make_prediction(img):
    # img = Image
    img = img.resize((28,28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape((1,28,28,1))
    img = img / 255.0
    res = model.predict([img])
    res = res[0]
    return np.argmax(res), max(res)

























# from keras import load_model
# from tkinter import *
# import tkinter as tk
# import win32gui
# from PIL import ImageGrab, Image, ImageOps
# import numpy as np
#
# model = load_model(" modell.h5")
# def make_prediction(imf):
#     img = img.resize((28,28))
#     img=img.convert('L')
#     img=np.array(img)
#     img=reshape((1,28,28,1))
#     img=img/255.0
#     res=model.prediction([img])
#     res=res[0]
#     return np.argmax(res), max(res)
#
# class App(tk.TK):
#     def __init__(self):
#         tk.TK.__init__(self)
#         self.x-self.y=0
#         self.canvas = tk.Canvas











'''

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''
