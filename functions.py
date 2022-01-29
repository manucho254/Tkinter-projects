from main import Toplevel,Tk,Label

def main_page(master,):
    main_win = Toplevel()
    main_win.geometry("800x600+200+50")
    master.deiconify()
    
def withdraw_and_create_window(master):
    master.withdraw()
    main_page(master)
    
