from main import *

class UserAuth(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("800x600+200+50")
        self.master.configure(bg="DarkSlateGray4")
        self.master.main_label = ttk.Label(self.master,  text="")
        self.label_frame = ttk.LabelFrame(self.master, text='Login', padding=20, width=600, height=300,  bootstyle=DARK)
        self.label_frame.pack(side=LEFT, expand=YES, padx=5, pady=5)
        self.label_username = ttk.Label(self.label_frame , text="Username", bootstyle=DARK, font="helvetica, 10")
        self.label_username.place(x=30,  y=40)
        self.entry_username = ttk.Entry(self.label_frame , width=50, bootstyle=DARK, font="helvetica, 10")
        self.entry_username.place(x=100,  y=40)
        self.label_username = ttk.Label(self.label_frame , text="Password", bootstyle=DARK, font="helvetica, 10")
        self.label_username.place(x=30,  y=110)
        self.entry_password = ttk.Entry(self.label_frame , width=50, bootstyle=DARK, font="helvetica, 10")
        self.entry_password.place(x=100,  y=110)
        self.login_button = ttk.Button(self.label_frame, text='Login', bootstyle=DARK, width=40,  )
        self.login_button.place(x=120,  y=200)

        
if __name__ == "__main__":
    main_gui(UserAuth)
        
            