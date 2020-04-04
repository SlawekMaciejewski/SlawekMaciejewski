import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Kilometres to miles converter")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a length in kilometres")
        self.km_entry = tkinter.Entry(self.top_frame, width=15)

        self.prompt_label.pack(side="left")
        self.km_entry.pack(side="left")

        self.conv_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.conv_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def convert(self):
        km = float(self.km_entry.get())
        miles = km * 0.6214
        self.display_result(km, miles)

    def display_result(self, km, miles):
        tkinter.messagebox.showinfo("Result", f'The {km} kilometres is {round(miles, 4)} miles.')


if __name__ == '__main__':
    my_gui = MyGUI()
