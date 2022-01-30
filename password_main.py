from main import *

class PASS_MAIN(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master
        
        self.site_label = ttk.Label(self.master, text="Webisite:", bootstyle=DARK, width=50, font="Sylfaen")
        self.site_label.place(x=10, y=40)
        self.site_entry_box = ttk.Entry(self.master, bootstyle=DARK, width=50)
        self.site_entry_box.place(x=120,  y=40)
        
        self.user_name_or_email_label = ttk.Label(self.master, text="Email or \nUsername:" , bootstyle=DARK, width=50, font="Sylfaen")
        self.user_name_or_email_label.place(x=10, y=90)
        self.user_name_or_email_entry_box = ttk.Entry(self.master, bootstyle=DARK, width=50)
        self.user_name_or_email_entry_box.place(x=120,  y=90)
        
        self.password_label = ttk.Label(self.master, text="Password", bootstyle=DARK, width=50, font="Sylfaen")
        self.password_label.place(x=10, y=140)
        self.password_entry = ttk.Entry(self.master, bootstyle=DARK, width=50)
        self.password_entry.place(x=120,  y=142)
        
        #==============================
        self.pass_list = ttk.Treeview(self.master, bootstyle=DARK)
        self.pass_list.place(x=10, y=200)
        
        self.pass_list['columns'] = ('id', 'website', 'username/email', 'password')
        self.pass_list.column("#0", width=2,  stretch=NO, anchor=CENTER)
        self.pass_list.column("id",anchor=CENTER, width=80)
        self.pass_list.column("website",anchor=CENTER,width=150)
        self.pass_list.column("username/email",anchor=CENTER,width=150)
        self.pass_list.column("password",anchor=CENTER,width=150)

        self.pass_list.heading("#0",text="",anchor=CENTER)
        self.pass_list.heading("id",text="Id",anchor=CENTER)
        self.pass_list.heading("website",text="Website",anchor=CENTER)
        self.pass_list.heading("username/email",text="Username/Email",anchor=CENTER)
        self.pass_list.heading("password",text="Password",anchor=CENTER)
        

if __name__ == "__main__":
    main_gui(PASS_MAIN, "white")