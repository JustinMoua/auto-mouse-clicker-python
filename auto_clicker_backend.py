"""
FILE NAME: auto_clicker_frontend.py

AUTHOR(S): Justin Moua

PURPOSE: Acts as a backend for my auto clicker program. Utilizes multithreading to perform clicking.

NOTES:
"""

import time
import threading
import pynput.mouse
import pynput.keyboard
import auto_clicker_frontend as frontend

class AutoClickerBackend():
    def __init__(self):
        self.TOGGLE_KEY = pynput.keyboard.Key.f6 #pynput.keyboard.KeyCode(char="t")
        self.clicking = False
        self.mouse = pynput.mouse.Controller()
        self.armed = False
        self.cps = 5
        self.backend_safety = False

    def clicker(self):
        """Performs automated clicking based on the CPS value."""
        while True:
            if self.clicking and self.cps > 0:
                # print("Clicking...")

                self.mouse.click(pynput.mouse.Button.left, 1)
                time.sleep(1 / self.cps)
            else:
                # print("Standby...")
                time.sleep(0.1)

    def toggle_event(self, key):
        """Toggle for automatic clicking."""
        if key == self.TOGGLE_KEY:
            self.clicking = not self.clicking
            print(f"Clicking toggled: {'ON' if self.clicking else 'OFF'}")

    def run(self):
        """Runs automatic clicker and starts it. Creates necessary threads for auto clicking."""
        #starts clicker in a different thread, seperate from main thread.
        click_thread = threading.Thread(target=self.clicker, daemon=True)
        click_thread.start()

        with pynput.keyboard.Listener(on_press=self.toggle_event) as listener:
            listener.join()

    #ToDo: Add a function to set the toggled key.