from tkinter import *

class AutoClickerGui:
    def __init__(self, master): #master is our root object.
        my_frame = Frame(master)
        my_frame.pack()
        self.click_me = Button(master, text="Click Me!", command=self.clickme)
        self.click_me.pack(pady=20)

        self.safety_status = False
        init_safety_text = 'Enabled' if self.safety_status else 'Disabled'
        self.safety_button = Button(master, text=init_safety_text, command=self.safety)
        self.safety_button.pack(pady=50)

    def clickme(self):
        print("Look at you... you clicked a button!")

    def safety(self):
        if self.safety_status:
            self.safety_status = False
        else:
            self.safety_status = True
        new_safety_status = 'Enabled' if self.safety_status else 'Disabled'
        self.safety_button.config(text = new_safety_status)