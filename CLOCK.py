import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        
        # Create and configure the clock label
        self.clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
        self.clock_label.pack(anchor='center')
        
        # Update the time initially
        self.update_time()
    
    def update_time(self):
        """Update the clock label with the current time."""
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        # Schedule the update_time method to be called again after 1000ms (1 second)
        self.root.after(1000, self.update_time)

def main():
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
