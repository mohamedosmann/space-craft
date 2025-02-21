import tkinter as tk

class Dashboard:
    def __init__(self):
        self.window = tk.Tk()
        self.fuel_label = tk.Label(self.window, text="Fuel: 5000 kg")
        self.altitude_label = tk.Label(self.window, text="Altitude: 0 km")
        self.fuel_label.pack()
        self.altitude_label.pack()
        self.update_ui()

    def update_ui(self):
        # Simulate data updates
        self.window.after(1000, self.update_ui)

Dashboard().window.mainloop()