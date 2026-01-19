"""
FILE NAME: auto_clicker_frontend.py

AUTHOR(S): Justin Moua

PURPOSE: Acts as a front end for an my auto clicker program. Consists of a GUI and connection to the backend.

NOTES:
"""
import tkinter as tk
import tkinter.messagebox as messagebox
import auto_clicker_backend as backend

class AutoClickerFrontend:
    def __init__(self, master):
        """

        :param master: root Tkinter window.
        """
        #============Clicks Per Second============
        self.cps = 0

        cps_frame = tk.Frame(master)
        cps_frame.pack(pady=10, anchor="w")

        cps_label = tk.Label(cps_frame, text="Change CPS: ")
        cps_label.grid(row=0, column=0, padx=5)

        self.cps_user_input = tk.StringVar()
        cps_input_field = tk.Entry(cps_frame, textvariable=self.cps_user_input, width=10)
        cps_input_field.grid(row=0, column=1, padx=5)

        confirm_cps_button = tk.Button(cps_frame, text="Confirm CPS", command=self.confirm_cps)
        confirm_cps_button.grid(row=0, column=2, padx=5)

        #============Safety============
        safety_frame = tk.Frame(master)
        safety_frame.pack(pady=10, anchor="w")

        self.safety_status = False
        init_safety_text = 'Enabled' if self.safety_status else 'Disabled'

        self.safety_frame_label = tk.Label(safety_frame, text="Safety Status: " + init_safety_text)
        self.safety_frame_label.grid(row=0, column=0, padx=5)


        self.safety_button = tk.Button(safety_frame, text=f"Click to {'enable' if not self.safety_status else 'disable'}", command=self.safety)
        self.safety_button.grid(row = 0, column = 2, padx=5)

        #============Keybind============
        keybind_frame = tk.Frame(master)
        keybind_frame.pack(pady=10, anchor="w")

        self.keybind_display = tk.Label(keybind_frame, text="Current keybind: F6")
        self.keybind_display.grid(row=0, column=0, padx=5)

        self.keybind_confirm_button = tk.Button(keybind_frame, text="Change keybind", command=self.confirm_keybind)
        self.keybind_confirm_button.grid(row=0, column=1, padx=5)
        #============TEST============
        click_me_frame = tk.Frame(master)
        click_me = tk.Button(click_me_frame, text="Click Me!", command=self.clickme)
        click_me.pack(pady=6)

        #============INFO============
        info_frame = tk.Frame(master)
        info_frame.pack(pady=10)
        self.cps_display = tk.Label(info_frame, text= f"CPS: {self.cps}", font=(None, 25, "bold"))
        self.cps_display.grid(row=0, column=0, padx=5)

        clicking = False
        self.activity_status_label = tk.Label(info_frame, text=f"Status: {'Clicking' if clicking else 'On standby'}",
                                              font=(None, 25, "bold"))
        self.activity_status_label.grid(row=2, column=0, padx=5)


    def clickme(self):
        """
        For testing purposes. Delete later.

        :return:
        """
        print("Look at you... you clicked a button!")

    def safety(self):
        """
        Changes safety status of backend to enabled or disabled.

        :return:
        """
        if self.safety_status:
            self.safety_status = False
        else:
            self.safety_status = True
        update_safety_button_text = f"Click to {'enable' if not self.safety_status else 'disable'}"
        update_safety_label = f"Safety Status: {'Enabled' if self.safety_status else 'Disabled'}"
        self.safety_button.config(text = update_safety_button_text)
        self.safety_frame_label.config(text=update_safety_label)

    def confirm_cps(self):
        """Checks whether the user inputted a valid number for CPS."""
        try:
            cps = int(self.cps_user_input.get())
            if cps > 0:
                self.cps = cps
                self.cps_user_input.set("")
                self.cps_display.config(text=f"CPS: {self.cps}")
                tk.messagebox.showinfo("CPS Updated", f"CPS has been changed to {self.cps}")
            else:
                tk.messagebox.showerror("Invalid Input", "Please enter a number greater than 0 for CPS.")
                self.cps_user_input.set("")
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Please enter a valid number for CPS.")

    def confirm_keybind(self):
        """Enables the user to change the keybind that toggles automatic clicking."""
        #ToDo: This keybind is for the button that toggles automatic clicking.
        # I will need to add one later that changes the keybind of which key is being automatically clicked.
        popup = tk.Toplevel()
        popup.title("Press a key")

        label = tk.Label(popup, text="Press any key to set a keybind")
        label.pack(padx = 20, pady = 20)

        # detect key press
        def on_key(event):
            self.TOGGLE_KEY = event.keysym
            self.keybind_display.config(text=f"Current keybind: {self.TOGGLE_KEY}")
            popup.destroy()

        popup.bind("<Key>", on_key)
        popup.focus_set() #All keyboard input from the user will go to this instead of other.
        popup.grab_set() #prevents user from interacting with other things in the main window.

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = AutoClickerFrontend(root)
    root.mainloop()