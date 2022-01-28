from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji
    
def main_gui(my_class, backgound_color):
    root = Tk()
    gui = my_class(root)
    root.configure(bg=backgound_color)
    root.minsize(600, 400)
    root.maxsize(1400, 700)
    root.mainloop()