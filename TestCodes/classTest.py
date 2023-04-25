import tkinter as tk

class ParentWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text="This is the parent window.")
        self.label.pack()

        self.button = tk.Button(self, text="Open child window", command=self.open_child_window)
        self.button.pack()

    def open_child_window(self):
        # Create a child window
        child_window = ChildWindow(self)
        child_window.pack()

class ChildWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="This is the child window.")
        self.label.pack()

        # Get the data that was passed from the parent window
        self.data = parent.data

        # Display the data in the child window
        self.label.config(text="The data from the parent window is: {}".format(self.data))

if __name__ == "__main__":
    root = ParentWindow()
    root.mainloop()