from tkinter import Tk

class UserInterface:
    
    def __init__(self, title,height, width) -> None:
        self.title = title
        self.height = height
        self.width = width
        self.root = Tk()
    
    def setScreen(self):
        # root window title and dimension
        self.root.title(self.title)
        # Set geometry (widthxheight)
        self.root.geometry(f'{self.height}x{self.width}')
    
    def run(self):
        self.setScreen()
        # Code to add widgets will go here...
        self.root.mainloop()