import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.line_button = tk.Button(self.button_frame, text="Draw Line", command=self.select_line)
        self.line_button.pack(side=tk.LEFT)
        
        self.rect_button = tk.Button(self.button_frame, text="Draw Rectangle", command=self.select_rectangle)
        self.rect_button.pack(side=tk.LEFT)
        
        self.oval_button = tk.Button(self.button_frame, text="Draw Oval", command=self.select_oval)
        self.oval_button.pack(side=tk.LEFT)
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
        
        self.start_x = None
        self.start_y = None
        self.current_shape = None
        self.shape = None
        
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_shape)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        
    def select_line(self):
        self.current_shape = "line"
        
    def select_rectangle(self):
        self.current_shape = "rectangle"
        
    def select_oval(self):
        self.current_shape = "oval"
        
    def clear_canvas(self):
        self.canvas.delete("all")
        
    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.shape = None
        
    def draw_shape(self, event):
        if self.shape:
            self.canvas.delete(self.shape)
        
        if self.current_shape == "line":
            self.shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y)
        elif self.current_shape == "rectangle":
            self.shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y)
        elif self.current_shape == "oval":
            self.shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y)
            
    def end_draw(self, event):
        self.shape = None

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

