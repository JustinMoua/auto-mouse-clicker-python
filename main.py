import auto_clicker_backend as acb
import auto_clicker_gui as acg
from tkinter import *

def main():
    root = Tk()
    root.title('Auto Clicker')
    #root.iconbitmap('')
    root.geometry("400x400")
    e = acg.AutoClickerGui(root)
    root.mainloop()

if __name__ =="__main__":
    main()