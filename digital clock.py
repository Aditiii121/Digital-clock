import tkinter as tk
from tkinter import ttk
import time

class DigitalClock:
    def _init_(self, root):
        self.root = root
        self.root.title("Digital Clock")
        
        self.time_label = ttk.Label(self.root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
        self.time_label.pack(anchor='center')
        
        self.update_time()
    
    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

if _name_ == "_main_":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()