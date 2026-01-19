"""
FILE NAME: main.py

AUTHOR(S): Justin Moua

PURPOSE: Allows users to perform automatic clicks of their desired button and clicks per second.

NOTES:
"""
import auto_clicker_backend as acb
import auto_clicker_frontend as acg
import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Auto Clicker')
    #root.iconbitmap('')
    root.geometry("400x400")
    e = acg.AutoClickerFrontend(root)
    root.mainloop()

if __name__ =="__main__":
    main()