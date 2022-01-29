from turtle import width
from main import *
from tkinter import Tk, font
from tkinter.messagebox import showerror, showinfo
from functions import main_page, withdraw_and_create_window

class UserAuth(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("800x600+200+50")
        self.master.resizable(width=0, height=0)
            
        self.master.main_label = ttk.Label(self.master, text="Password Manager", bootstyle=DARK, font="Sylfaen, 40")
        self.master.main_label.place(x=170, y=40)
        self.label_frame = ttk.LabelFrame(self.master, text='Login',  padding=20, width=600, height=300,  bootstyle=DARK)
        self.label_frame.pack(side=LEFT, expand=YES)
        self.label_username = ttk.Label(self.label_frame , text="Username", bootstyle=DARK, font="Sylfaen, 10")
        self.label_username.place(x=30,  y=40)
        self.entry_username = ttk.Entry(self.label_frame , width=50, bootstyle=DARK, font="Sylfaen, 10")
        self.entry_username.place(x=100,  y=40)
        self.label_username = ttk.Label(self.label_frame , text="Password", bootstyle=DARK, font="Sylfaen, 10")
        self.label_username.place(x=30,  y=110)
        self.entry_password = ttk.Entry(self.label_frame , width=50, bootstyle=DARK, font="Sylfaen, 10")
        self.entry_password.place(x=100,  y=110)
        self.login_button = ttk.Button(self.label_frame, text='Login', bootstyle=DARK, width=40, command=lambda:[withdraw_and_create_window(master)])
        self.login_button.place(x=120,  y=200)
        
        
if __name__ == "__main__":
    main_gui(UserAuth, "white")