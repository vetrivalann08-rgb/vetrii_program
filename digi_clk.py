import tkinter as tk
import time 
class DigiClk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.root.geometry("300x100")
        self.label = tk.Label(self.root, font=("Arial", 20), bg="white", fg="black")
        self.label.pack(expand=True)    

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def run(self):
        self.update_clock()
        self.root.mainloop()
if __name__ == "__main__":
    clock = DigiClk()
    clock.run() 

