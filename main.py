import tkinter


class MyGUI:
    def __init__(self):
        # Creating the main window.
        self.main_window = tkinter.Tk()
        # Creating a widget Label with the message
        self.label1 = tkinter.Label(self.main_window, text="Hello world!")
        self.label2 = tkinter.Label(self.main_window, text="This is GUI!")
        # Call to method pack() on the widget Label.
        self.label1.pack(side='right')  # 'bottom', 'top'
        self.label2.pack(side='left')
        # Entrance to the main loop
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()
