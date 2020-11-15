import sqlite3
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pandas as pd




class Main_GUI_core(Frame):
    def __init__(self, master):
        super().__init__(master)
        data = ProfitTable().get_all_data()

        f_top = Frame(self)
        #date
        f1 = LabelFrame(f_top, text = 'select date')
        l1 = Label(f1, text = 'start:')
        l2 = Label(f1, text = 'end:')
        self.e1 = Entry(f1)
        self.e2 = Entry(f1)


        f_top.pack(expand = True, fill = 'both')
        f2.pack(expand = True, fill = 'both')
        f3.pack(expand = True, fill = 'both')

        self.e1.insert('end', '2021-08-01')
        self.e2.insert('end', date.today())





    def on_bar(self):
        pass



    def on_piechart(self):
        pass

    def on_add_item(self):
        pass

def main():
    root = Tk()
    app = Main_GUI_core(root)
    app.pack(expand = True, fill = 'both')

    root.mainloop()


if __name__ == '__main__':
    main()
