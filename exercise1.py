import tkinter


class MyGUI:
    def __init__(self):
        # Creating the main window.
        self.main_window = tkinter.Tk()

        # Creating a widget Frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Creating a widget Label with the message into Frame
        self.label1 = tkinter.Label(self.top_frame, text="Hello world!")
        self.label2 = tkinter.Label(self.top_frame, text="This is GUI!")
        self.label3 = tkinter.Label(self.top_frame, text="This is first APP!")

        self.label4 = tkinter.Label(self.bottom_frame, text="Winken")
        self.label5 = tkinter.Label(self.bottom_frame, text="Blinken")
        self.label6 = tkinter.Label(self.bottom_frame, text="Nod")

        # Call to method pack() on the widget Label.
        self.label1.pack(side='right')  # 'bottom', 'top'
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        self.label4.pack(side='top')
        self.label5.pack(side='bottom')
        self.label6.pack(side='top')


        # Call to method pack() on the widget Frame.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Entrance to the main loop
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()
