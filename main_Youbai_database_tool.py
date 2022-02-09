import sqlite3
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pandas as pd
from pandastable import Table
import numpy as np
from datetime import date

from profitTable import ProfitTable
from profitStatistic import ProfitStatic
from main_GUI_core import Main_GUI_core
from additem import Additem

class Main_GUI(Main_GUI_core):
    def __init__(self, master):
        super().__init__(master)


    def on_bar(self):
        statictics = ProfitStatic(Toplevel())
        df6 = ProfitTable().get_sorted_profit_group()
        names = {'num':'item numbers', 'price_average': 'delivery price per package', 'tb_price':'total buy price', 'tc_price': 'total sell price', 'profit':'total profit'}
        for i, colName in enumerate(names.items()):
            statictics.plot_bar(statictics.ax[i], df6,colName)



    def on_piechart(self):
        statictics = ProfitStatic(Toplevel())
        df6 = ProfitTable().get_sorted_profit_group()
        legend = False
        names = {'num':'item numbers', 'price_average': 'delivery price per package', 'tb_price':'total buy price', 'tc_price': 'total sell price', 'profit':'total profit'}
        for i, colName in enumerate(names.items()):

            if i==0:
                legend = True
            else:
                legend = False
            statictics.plot_piechart(statictics.ax[i], df6,colName, legend)


    def on_add_item(self):
        w= Toplevel()
        w.title('add new data to database')
        add = Additem(w)
        add.pack(expand = True, fill = 'both')


def main():
    root = Tk()
    app = Main_GUI(root)
    app.pack(expand = True, fill = 'both')

    # app.on_bar()

    root.mainloop()


if __name__ == '__main__':
    main()
