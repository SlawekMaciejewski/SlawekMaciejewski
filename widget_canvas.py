import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.window2 = tkinter.Tk()
        self.window3 = tkinter.Tk()
        self.window4 = tkinter.Tk()
        self.window5 = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        self.canvas.pack()
        self.canvas.create_line(0, 0, 199, 199, width=5, smooth=True, fill='green', arrow='both')
        self.canvas.create_line(199, 0, 0, 199, dash=(5, 2))
        points = [30, 10, 170, 10, 100, 80, 30, 10]
        self.canvas.create_line(points, fill='cyan')

        self.canvas2 = tkinter.Canvas(self.window2, width=200, height=200)
        self.canvas2.pack()
        self.canvas2.create_rectangle(10, 10, 190, 190, width=5, fill='blue', outline='red')

        self.canvas3 = tkinter.Canvas(self.window3, width=200, height=200)
        self.canvas3.pack()
        self.canvas3.create_oval(10, 10, 190, 150, fill='white')
        self.canvas3.create_oval(50, 30, 150, 130, fill='gold', dash=(3, 2))

        self.canvas4 = tkinter.Canvas(self.window4, width=200, height=200)
        self.canvas4.pack()
        self.canvas4.create_arc(20, 20, 180, 180, start=90, extent=45, style='pieslice', fill='blue')
        self.canvas4.create_arc(20, 20, 180, 180, start=0, extent=60, style='arc', width=2)
        self.canvas4.create_arc(20, 20, 180, 180, start=270, extent=45, style='chord', fill='grey')
        self.canvas4.create_arc(20, 20, 180, 180, start=180, extent=45, width=3, outline='red')

        self.canvas5 = tkinter.Canvas(self.window5, width=200, height=200)
        self.canvas5.pack()
        points_polygon = (60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60)
        self.canvas5.create_polygon(points_polygon, fill='white', outline='blue')



        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()
