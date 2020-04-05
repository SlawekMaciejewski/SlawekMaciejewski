import tkinter
import tkinter.messagebox


class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Radio Buttons")

        self.top_frame = tkinter.Frame(self.main_window, borderwidth=4, relief="sunken")
        self.bottom_frame = tkinter.Frame(self.main_window, borderwidth=4, relief="sunken")

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(3)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text="Option 1", variable=self.radio_var,
                                       value=1)  # command=self.my_method
        self.rb2 = tkinter.Radiobutton(self.top_frame, text="Option 2", variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text="Option 3", variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("You choice", f'Option number: {str(self.radio_var.get())}')
        pass


if __name__ == '__main__':
    my_gui = MyGUI()
