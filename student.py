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
        self.label = Label(self.label_frame, text="label in labelframe", width=100)
        self.label.pack(side="top")
        
if __name__ == "__main__":
    main_gui(Student)