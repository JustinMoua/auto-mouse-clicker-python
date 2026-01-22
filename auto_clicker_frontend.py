"""
FILE NAME: auto_clicker_frontend.py

AUTHOR(S): Justin Moua

PURPOSE: Acts as a front end for an my auto clicker program. Consists of a GUI and connection to the backend.

NOTES:
"""
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import auto_clicker_backend as backend
from PIL import Image, ImageTk

class AutoClickerFrontend:
    def __init__(self, master):
        #ToDo: Add options to allow user to indicate what button they want pressed. Can be keyboard or Mouse.
        #ToDo: Brainstorm if I want to allow the user to press multiple buttons at the same time, and seperately.

        self.master = master

        self.client_screen_width = master.winfo_screenwidth()
        self.client_screen_height = master.winfo_screenheight()

        screen_width = self.client_screen_width * 0.25
        screen_height = self.client_screen_height * 0.5
        master.geometry(f"{int(screen_width)}x{int(screen_height)}")

        #INFO STATS
        info_frame = tk.LabelFrame(master, text="Info", padx=10, pady=10)
        info_frame.pack(fill="x", pady=10, padx=10)

        for r in range(3):
            info_frame.grid_rowconfigure(r, pad=5)

        original_image = Image.open(r".\external\images\info.png")
        resized_image = original_image.resize((25,25), Image.Resampling.LANCZOS)

        self.info_icon = ImageTk.PhotoImage(resized_image)
        self._cps_ui(info_frame)
        self._safety_ui(info_frame)
        self._keybind_ui(info_frame)

        #LIVE STATS
        live_stats_frame = tk.LabelFrame(master, text="Live Stats", padx=10, pady=10)
        live_stats_frame.pack(fill="x", pady=10, padx=10)

        for r in range(3):
            info_frame.grid_rowconfigure(r, pad=5)

        self._timer_ui(live_stats_frame)
        self._total_clicks_ui(live_stats_frame)

        #REST OF UI
        #ToDo: Make this change so that it says "Clicking..." when the program is running.
        application_status = tk.Frame(master, bd=2)
        application_status.pack(fill="x", padx=10, pady=10)

        status_label = tk.Label(
            application_status,
            text="On Standby...",
            font=("Arial", 20, "bold")
        )
        status_label.pack(pady=10)

        self.toggle_key = "F6" #ToDo:
                               # Ensure that toggle_key is changed when button is clicked.
                               # Currently displays the change but I don't think I remembered
                               # to adjust change here too. This will be passed to the backend.
        self.cps = 0           #ToDo: Reminder to self that cps is already changed when button is clicked.
        self.safety = True     #ToDo: Ensure safety is changed when button is clicked. Same reason as toggle_key.

    #INFO
    def run(self):
        self.master.mainloop()

    def _info_popup(self, title, message):
        """Pops up a window to display information about UI elements."""
        popup = tk.Toplevel()
        popup.title(title)
        screen_width = self.client_screen_width * 0.15
        screen_height = self.client_screen_height * 0.10
        # popup.geometry("300x120")
        popup.geometry(f"{int(screen_width)}x{int(screen_height)}")

        label = tk.Label(popup, text=message, wraplength=280, justify="left")
        label.pack(padx=10, pady=10)

        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=(0, 10))

    def _cps_ui(self, parent):
        """UI for CPS"""
        #Label
        cps_label = tk.Label(parent, text="Current CPS")
        cps_label.grid(row=0, column=0, padx=5, sticky="w")

        #Value
        self.cps_display = tk.Entry(
            parent,
            width=8,
            readonlybackground="white",
            justify="right"
        )
        self.cps_display.insert(0, "0")
        self.cps_display.config(state="readonly")
        self.cps_display.grid(row=0, column=1, padx=5)

        #Button
        cps_button = tk.Button(parent, text="Modify CPS", command=self.modify_cps)
        cps_button.grid(row = 0, column = 2, padx=5, sticky="w")

        title = "CPS"
        description = "Set the amount of\nclicks per second."
        info = tk.Button(parent, image=self.info_icon, bd=0, command=lambda: self._info_popup(title, description))
        info.grid(row=0, column=3, padx=5)

    def _safety_ui(self, parent):
        """UI for safety enabling/disabling"""
        #Label
        self.safety_status = True
        tk.Label(parent, text="Safety: ").grid(row=1, column=0, padx=5, sticky="w")

        #Value
        self.safety_status_display = tk.Entry(
            parent,
            width=8,
            readonlybackground="white",
            justify="right"
        )
        self.safety_status_display.insert(0, "Enabled")
        self.safety_status_display.config(state="readonly")
        self.safety_status_display.grid(row=1, column=1, padx=5)

        #Button
        self.safety_button = tk.Button(parent, text=f"Click to {'enable' if not self.safety_status else 'disable'}", command=self.modify_safety)
        self.safety_button.grid(row = 1, column = 2, padx=5, sticky="w")

        title = "Safety"
        description = "The safety button enables or disables safety mode. When enabled, it stops the auto clicker from clicking which might interfere with the keybind you use (such as when texting somebody)."
        info = tk.Button(parent, image=self.info_icon, bd=0, command=lambda: self._info_popup(title, description))
        info.grid(row=1, column=3, padx=5)

    def _keybind_ui(self, parent):
        """UI to allow user to select keybind to activate toggling"""
        #Label
        self.keybind_label = tk.Label(parent, text="Current keybind ")
        self.keybind_label.grid(row=2, column=0, padx=5)

        #Value
        self.keybind_display = tk.Entry(
            parent,
            width=8,
            readonlybackground="white",
            justify="right"
        )
        self.keybind_display.insert(0, "F6")
        self.keybind_display.config(state="readonly")
        self.keybind_display.grid(row=2, column=1, padx=5)

        #Button
        keybind_button = tk.Button(parent, text="Change keybind", command=self.modify_keybind)
        keybind_button.grid(row=2, column=2, padx=5, sticky="w")

        title = "Changing your keybind"
        description = "Keybind the desired key on your keyboard to turn on and turn off the auto clicker."
        info = tk.Button(parent, image=self.info_icon, bd=0,command=lambda: self._info_popup(title, description))
        info.grid(row=2, column=3, padx=5)

    def modify_cps(self):
        """Front end UI that changes the CPS of the auto clicker."""
        popup = tk.Toplevel()
        popup.title("Enter a number to set CPS")

        label = tk.Label(popup, text="Enter a number:")
        label.pack(padx=20, pady=(20, 5))

        # Entry field
        cps_entry = tk.Entry(popup, width=10, justify="center")
        cps_entry.pack(padx=20, pady=(0, 10))
        cps_entry.focus_set()

        def confirm():
            try:
                cps_value = int(cps_entry.get())
                if cps_value > 0:
                    self.cps = cps_value
                    popup.destroy()
                    self.cps_display.config(state="normal")
                    self.cps_display.delete(0, tk.END)
                    self.cps_display.insert(0, str(cps_value))
                    self.cps_display.config(state="readonly")
                else:
                    tk.messagebox.showerror("Invalid Input", "Please enter a number greater than 0.")
            except ValueError:
                tk.messagebox.showerror("Invalid Input", "Please enter a valid number.")

        confirm_button = tk.Button(popup, text="Confirm", command=confirm)
        confirm_button.pack(padx=20, pady=(0, 20))

        popup.grab_set()
        popup.focus_set()

    def modify_safety(self):
        """Changes safety status of backend to enabled or disabled."""
        if self.safety_status:
            self.safety_status = False
        else:
            self.safety_status = True
        update_button_text = f"Click to {'enable' if not self.safety_status else 'disable'}"
        self.safety_button.config(text = update_button_text)

        self.safety_status_display.config(state="normal")
        self.safety_status_display.delete(0, tk.END)
        self.safety_status_display.insert(0, f"{'Enabled' if self.safety_status else 'Disabled'}")
        self.safety_status_display.config(state="readonly")

    def modify_keybind(self):
        """Enables the user to change the keybind that toggles automatic clicking."""
        popup = tk.Toplevel()
        popup.title("Press a key")

        label = tk.Label(popup, text="Press any key to set a keybind")
        label.pack(padx = 20, pady = 20)

        # detect key press
        def on_key(event):
            TOGGLE_KEY = event.keysym
            self.keybind_display.config(text=f"Current keybind {TOGGLE_KEY}")

            self.keybind_display.config(state="normal")
            self.keybind_display.delete(0, tk.END)
            self.keybind_display.insert(0, f"{TOGGLE_KEY}")
            self.keybind_display.config(state="readonly")

            popup.destroy()

        popup.bind("<Key>", on_key)
        popup.focus_set() #All keyboard input from the user will go to this instead of other.
        popup.grab_set() #prevents user from interacting with other things in the main window.

    #LIVE
    def _timer_ui(self, parent):
        """
        Displays the total elapsed time of the current session of clicking.

        :param parent:  Parent widget to attach UI elements to.
        :return:
        """
        #Label
        timer_label = tk.Label(parent, text="Time Elapsed ")
        timer_label.grid(row=0, column=0, padx=5, sticky="w")

        #Value
        self.timer_display = tk.Entry(
            parent,
            width=8,
            readonlybackground="white",
            justify="right"
        )
        self.timer_display.insert(0, "0s")
        self.timer_display.config(state="readonly")
        self.timer_display.grid(row=0, column=1, padx=5)

        title = "Timer"
        description = "Displays how long the autoclicker has been running"
        info = tk.Button(parent, image=self.info_icon, bd=0, command=lambda: self._info_popup(title, description))
        info.grid(row=0, column=3, padx=5)

    def _total_clicks_ui(self, parent):
        """
        Displays the total clicks elapsed of the current session of clicking.

        :param parent: Parent widget to attach UI elements to.
        :return:
        """
        #Label
        tot_clicks_label = tk.Label(parent, text="Clicks Elapsed ")
        tot_clicks_label.grid(row=1, column=0, padx=5, sticky="w")

        #Value
        self.tot_clicks_display = tk.Entry(
            parent,
            width=8,
            readonlybackground="white",
            justify="right"
        )
        self.tot_clicks_display.insert(0, "0")
        self.tot_clicks_display.config(state="readonly")
        self.tot_clicks_display.grid(row=1, column=1, padx=5)

        title = "Total Clicks"
        description =  "Displays your total clicks in your current session."
        info = tk.Button(parent, image=self.info_icon, bd=0, command=lambda: self._info_popup(title,description))
        info.grid(row=1, column=3, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Justin Moua's Auto Clicker")
    AutoClicker = AutoClickerFrontend(root)
    AutoClicker.run()