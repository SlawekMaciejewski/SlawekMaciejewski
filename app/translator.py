"""
Simply app with buttons and labels to translate words Latin to English.
"""
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.desc_label = tkinter.Label(self.top_frame, text="Choose a Latin word to translate:")
        self.desc_label.pack()

        self.w1_button = tkinter.Button(self.mid_frame, text='sinister', command=self.translate1)
        self.w2_button = tkinter.Button(self.mid_frame, text='medium', command=self.translate2)
        self.w3_button = tkinter.Button(self.mid_frame, text='dexter', command=self.translate3)

        self.w1_button.pack(side='left')
        self.w2_button.pack(side='left')
        self.w3_button.pack(side='left')

        self.label = tkinter.Label(self.bottom_frame, text="English translation: ")
        self.translate = tkinter.StringVar()
        self.translate_label = tkinter.Label(self.bottom_frame, textvariable=self.translate)
        self.label.pack(side='left')
        self.translate_label.pack(side='left')

        tkinter.mainloop()

    def translate1(self):
        self.translate.set("left")

    def translate2(self):
        self.translate.set("medium")

    def translate3(self):
        self.translate.set("right")


if __name__ == '__main__':
    my_gui = MyGUI()
