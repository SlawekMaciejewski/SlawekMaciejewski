import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.window2 = tkinter.Tk()
        self.window3 = tkinter.Tk()
        self.window4 = tkinter.Tk()

        self.cnavas = tkinter.Canvas(self.main_window, width=200, height=200)
        self.cnavas.pack()
        self.cnavas.create_line(0, 0, 199, 199, width=5, smooth=True, fill='green', arrow='both')
        self.cnavas.create_line(199, 0, 0, 199, dash=(5, 2))
        points = [30, 10, 170, 10, 100, 80, 30, 10]
        self.cnavas.create_line(points, fill='cyan')

        self.cnavas2 = tkinter.Canvas(self.window2, width=200, height=200)
        self.cnavas2.pack()
        self.cnavas2.create_rectangle(10, 10, 190, 190, width=5, fill='blue', outline='red')

        self.cnavas3 = tkinter.Canvas(self.window3, width=200, height=200)
        self.cnavas3.pack()
        self.cnavas3.create_oval(10, 10, 190, 150)
        self.cnavas3.create_oval(50, 50, 150, 150, fill='gold', dash=(3, 2))

        self.cnavas4 = tkinter.Canvas(self.window4, width=200, height=200)
        self.cnavas4.pack()
        self.cnavas4.create_arc(20, 20, 180, 180, start=90, extent=45, style='pieslice', fill='blue')
        self.cnavas4.create_arc(20, 20, 180, 180, start=0, extent=60, style='arc', width=2)
        self.cnavas4.create_arc(20, 20, 180, 180, start=270, extent=45, style='chord', fill='grey')
        self.cnavas4.create_arc(20, 20, 180, 180, start=180, extent=45, width=3, outline='red')

        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
