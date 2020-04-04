import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Kilometres to miles converter")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a length in kilometres")
        self.km_entry = tkinter.Entry(self.top_frame, width=15)
        self.descr_label = tkinter.Label(self.mid_frame, text="Result of conversion: ")

        self.prompt_label.pack(side="left")
        self.km_entry.pack(side="left")

        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.descr_label.pack(side="left")
        self.miles_label.pack(side="left")

        self.conv_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.conv_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def convert(self):
        km = float(self.km_entry.get())
        miles = km * 0.6214
        self.value.set(round(miles, 4))




if __name__ == '__main__':
    my_gui = MyGUI()
