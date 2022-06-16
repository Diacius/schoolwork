from tkinter import *
from time import sleep
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = Window(root)
root.wm_title('Text Editor')
root.geometry('1000x700')
lbl1 = Label(root, text=u"🙂🟪Test")
lbl1.grid()




# Run last
root.mainloop()
