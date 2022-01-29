from main import *

class Student(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.width = 1000
        self.height = 600
        self.master.geometry(f"{self.width}x{self.height}+200+50")
        self.master.title("Student Management System")
        self.label_frame = LabelFrame(self.master, text="Dashboard", width=500,  height=self.height)
        self.label_frame.place(x=0, y=0)
        self.label = Label(self.label_frame, text="label in labelframe", width=50)
        self.label.grid(column=0, row=1)
        self.student_add_button = ttk.Button(self.master, text=f"Add student +",  bootstyle=DARK)
        self.student_add_button.place(x=500, y=0)
        self.student_list = ttk.Treeview(self.master, bootstyle=DARK)
        self.student_list.place(x=300, y=400)
        
        #==============================
        self.student_list['columns'] = ('student_id', 'student_name', 'student_class', 'student_parent', 'student_parent_number')
        self.student_list.column("#0", width=2,  stretch=NO, anchor=CENTER)
        self.student_list.column("student_id",anchor=CENTER, width=80)
        self.student_list.column("student_name",anchor=CENTER,width=150)
        self.student_list.column("student_class",anchor=CENTER,width=150)
        self.student_list.column("student_parent",anchor=CENTER,width=150)
        self.student_list.column("student_parent_number",anchor=CENTER,width=150)

        self.student_list.heading("#0",text="",anchor=CENTER)
        self.student_list.heading("student_id",text="Id",anchor=CENTER)
        self.student_list.heading("student_name",text="Name",anchor=CENTER)
        self.student_list.heading("student_class",text="class" ,anchor=CENTER)
        self.student_list.heading("student_parent",text="Parent's Name",anchor=CENTER)
        self.student_list.heading("student_parent_number",text="Parent's phone:",anchor=CENTER)

        
if __name__ == "__main__":
    main_gui(Student, "white")