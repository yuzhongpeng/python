import os
from tkinter import *
from tkinter.filedialog import askopenfilenames

def selectPath(): # 选择文件路径
    path_ = askopenfilenames()
    path.set(path_)

root = Tk()
root.title('Ftp tool')
root.resizable()
path = StringVar()


Label(root, text = '目标路径:').grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = '路径选择', command = selectPath).grid(row = 0, column = 2)










root.mainloop()
