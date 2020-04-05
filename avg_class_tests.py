import tkinter


class TestAvg:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Calculate average")

        self.top1_frame = tkinter.Frame(self.main_window)
        self.top2_frame = tkinter.Frame(self.main_window)
        self.top3_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top1_frame.pack()
        self.top2_frame.pack()
        self.top3_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.test1_label = tkinter.Label(self.top1_frame, text="Provide score test 1: ")
        self.test1_entry = tkinter.Entry(self.top1_frame, width=10)

        self.test1_label.pack(side="left")
        self.test1_entry.pack(side="left")

        self.test2_label = tkinter.Label(self.top2_frame, text="Provide score test 2: ")
        self.test2_entry = tkinter.Entry(self.top2_frame, width=10)

        self.test2_label.pack(side="left")
        self.test2_entry.pack(side="left")

        self.test3_label = tkinter.Label(self.top3_frame, text="Provide score test 3: ")
        self.test3_entry = tkinter.Entry(self.top3_frame, width=10)

        self.test3_label.pack(side="left")
        self.test3_entry.pack(side="left")

        self.result_label = tkinter.Label(self.mid_frame, text="The average of the tests is: ")
        self.value_avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.mid_frame, textvariable=self.value_avg)

        self.result_label.pack(side="left")
        self.avg_label.pack(side="left")

        self.calc_button = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calc_avg)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def calc_avg(self):
        sum = float(self.test1_entry.get()) + float(self.test2_entry.get()) + float(self.test3_entry.get())
        avg = round(sum / 3, 2)
        self.value_avg.set(avg)


if __name__ == '__main__':
    test_avg = TestAvg()
