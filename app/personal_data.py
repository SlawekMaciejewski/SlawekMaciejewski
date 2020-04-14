"""
Simply app with buttons to "show info" and "quit".
"""
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.info = tkinter.StringVar()
        self.show_label = tkinter.Label(self.top_frame, textvariable=self.info)
        self.show_label.pack()

        self.show_button = tkinter.Button(self.bottom_frame, text='Show info', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')

        tkinter.mainloop()

    def show_info(self):
        self.info.set("Slawek Maciejewski \n Lodz \n Poland")


if __name__ == '__main__':
    my_gui = MyGUI()
