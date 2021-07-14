import matplotlib.figure
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog


class main:
    def __init__(self, window):
        m1 = tkinter.PanedWindow(window, orient=tkinter.HORIZONTAL)
        m1.pack(fill='both', expand=True)

        # controlFrame setting
        controlFrame = tkinter.PanedWindow(m1)
        controlFrame.pack(side='left', fill='both', expand=False)
        m1.add(controlFrame)
        m2 = tkinter.PanedWindow(m1, orient=tkinter.VERTICAL)
        m2.pack(fill='both', expand=False)
        m1.add(m2)

        # plotFrame setting
        plotFrame = tkinter.Frame(m2)
        plotFrame.pack(side='right', fill='both', expand=True)
        m2.add(plotFrame, stretch='always')

        # controlFrame inner Frame setting
        varFrame = tkinter.PanedWindow(controlFrame)
        varFrame.pack(side='top', fill='x')
        self.inputFrame = tkinter.PanedWindow(controlFrame)
        self.inputFrame.pack(side='top', fill='x')
        buttonFrame = tkinter.PanedWindow(controlFrame)
        buttonFrame.pack(side='top', fill='x')
        # controlFrame var setting
        i = 0
        option = ['acr', 'acr_hor']
        option.sort()
        while i < len(option):
            option[i] = str(i+1) + '.' + option[i]
            i += 1
        self.var = tkinter.StringVar()
        self.var = tkinter.ttk.Combobox(
            varFrame, textvariable=self.var, values=option)
        self.var_index = 0
        if len(option) != 0:
            self.var.current(0)
        self.var.pack(fill='x', side='left')
        tkinter.Button(varFrame, text='confirm',
                       command=self.confirm, width=10).pack(side='right', fill='x')
        # controlFrame inputFrame setting
        inputFrame_1 = tkinter.PanedWindow(self.inputFrame)
        inputFrame_1.pack(fill='x')
        label1 = tkinter.Label(inputFrame_1, text="v0").pack(side='left')
        self.num_area_1 = tkinter.Entry(
            master=inputFrame_1, width=5, font=20)
        self.num_area_1.pack(side='right')
        inputFrame_2 = tkinter.PanedWindow(self.inputFrame)
        inputFrame_2.pack(fill='x')
        label2 = tkinter.Label(inputFrame_2, text="rad").pack(side='left')
        self.num_area_2 = tkinter.Entry(
            inputFrame_2, width=5, font=20)
        self.num_area_2.pack(side='right')
        self.inputFrame_3_index = 0
        # controlFrame buttonFrame setting
        tkinter.Button(buttonFrame, text="add",
                       command=self.add, width=10).pack(anchor='center', fill='x')
        tkinter.Button(buttonFrame, text='clear', command=self.clear, width=10).pack(
            anchor='center', fill='x')

        # link plotFrame pyplot
        fig = matplotlib.figure.Figure()
        self.canvas = FigureCanvasTkAgg(fig, master=plotFrame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        NavigationToolbar2Tk(self.canvas, plotFrame).update()
        self.ax1 = fig.add_subplot()

    def confirm(self):
        from functools import partial

        self.var_index = self.var.get()
        # print(self.var_index)

        if self.var_index == '2.acr_hor' and self.inputFrame_3_index == 0:
            print('t')
            self.inputFrame_3 = tkinter.PanedWindow(self.inputFrame)
            self.inputFrame_3.pack(fill='x')
            self.label3 = tkinter.Label(
                self.inputFrame_3, text='height').pack(side='left')
            self.num_area_3 = tkinter.Entry(
                self.inputFrame_3, width=5, font=20)
            self.num_area_3.pack(side='right')
            self.inputFrame_3_index = 1
        elif self.var_index == '1.acr' and self.inputFrame_3_index == 1:
            self.remove(self.inputFrame_3)

    def add(self):
        if self.var_index == '1.acr':
            self.acr()
        elif self.var_index == '2.acr_hor':
            self.arc_hor()

    def acr(self):
        import math
        import numpy as np

        temp = float(self.num_area_2.get())
        v0 = float(self.num_area_1.get())
        rad = (temp/180) * math.pi

        g = 9.8
        ftime = (2 * v0 * math.sin(rad)) / g
        t_list = np.arange(0, ftime, 0.001)

        tempx = (v0 * math.cos(rad)) * t_list
        tempy_1 = np.array(t_list * (v0*math.sin(rad)))
        tempy_2 = np.array(t_list**2)
        tempy = tempy_1 - tempy_2*(g/2)

        # print(x, y)
        # height = (v0**2) * (math.sin(rad)**2) / (2 * g)
        self.ax1.plot(tempx, tempy)
        self.canvas.draw()

    def arc_hor(self):
        import math
        import numpy as np

        g = 9.8
        v0 = float(self.num_area_1.get())
        temp = float(self.num_area_2.get())
        rad = (temp/180)*math.pi
        height = float(self.num_area_3.get())
        max_height = height + ((v0**2)*(math.sin(rad)**2)/(2*g))

        time = ((2*max_height)/g)**(1/2) + ((v0*math.sin(rad))/g)
        t_list = np.arange(0, time, 0.001)

        tempx = np.array((v0 * math.cos(rad))*t_list)
        tempy_1 = np.array((v0 * math.sin(rad)) * t_list)
        tempy_2 = np.array(t_list**2)
        tempy = height+(tempy_1 - tempy_2*(g/2))

        self.ax1.plot(tempx, tempy)
        self.canvas.draw()

    def clear(self):
        self.ax1.clear()
        self.canvas.draw()

    def remove(self, frame):
        frame.destroy()
        self.frames.remove(frame)


window = tkinter.Tk()
start = main(window)
tkinter.mainloop()
