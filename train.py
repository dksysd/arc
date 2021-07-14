from functools import partial

from tkinter import *
from tkinter import ttk


class Database(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # parent.state("zoomed")
        self.parent = parent

        MainFrame = Frame(self)
        MainFrame.pack(expand=True, side="top", fill="both")

        self.frames = []

        DataFrameAF = LabelFrame(MainFrame, text="Information")
        DataFrameAF.pack(side="top", pady=10, expand=True, fill="both")

        self.canvas = Canvas(DataFrameAF, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        vsb = Scrollbar(DataFrameAF, orient="vertical",
                        command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((20, 20), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", self.reset_scrollregion)

        # Button for adding New Subframe
        self.NewButton = Button(self.frame, text="New", command=self.new)
        self.NewButton.pack(side="bottom", fill="x")

    def reset_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def new(self):
        global widgetNames
        global frameNames

        DataFrameAF_ = LabelFrame(self.frame, bg="blue", text="Sub Info")
        DataFrameAF_.pack(side="top", padx=10, pady=10,
                          fill="both", expand=True)

        self.frames.append(DataFrameAF_)

        DataFrameAc = Frame(DataFrameAF_)
        DataFrameAc.pack(side="left", padx=5)

        self.lbl_1 = Label(
            DataFrameAc, text="A1                                    ")
        self.lbl_1.grid(row=1, column=0, sticky="w")

        self.txt_1 = ttk.Entry(DataFrameAc, width=20)
        self.txt_1.grid(row=1, column=1)

        self.lbl_2 = Label(
            DataFrameAc, text="A2                                    ")
        self.lbl_2.grid(row=2, column=0, sticky="w")

        self.txt_2 = ttk.Entry(DataFrameAc, width=20)
        self.txt_2.grid(row=2, column=1)

        self.lbl_3 = Label(
            DataFrameAc, text="B1                                    ")
        self.lbl_3.grid(row=1, column=2, sticky="w")

        self.txt_3 = ttk.Entry(DataFrameAc, width=20)
        self.txt_3.grid(row=1, column=3)

        self.lbl_4 = Label(
            DataFrameAc, text="B2                                    ")
        self.lbl_4.grid(row=2, column=2, sticky="w")

        self.txt_4 = ttk.Entry(DataFrameAc, width=20)
        self.txt_4.grid(row=2, column=3)

        # remove the New Button and include the Add button inside the new subframe
        self.NewButton.pack_forget()
        AddButton = Button(DataFrameAF_, text="ADD", command=self.new)
        AddButton.pack(side="bottom")

        remove_button = Button(DataFrameAF_, text="Remove",
                               command=partial(self.remove, DataFrameAF_))
        remove_button.pack(side="top")

    def remove(self, frame):
        frame.destroy()
        self.frames.remove(frame)
        if len(self.frames) == 0:
            self.NewButton.pack()


root = Tk()
database_window = Database(root)
database_window.pack(side="top", fill="both", expand=True)
root.mainloop()
