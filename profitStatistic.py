from  tkinter import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import (
                                    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

from profitTable import ProfitTable
import pandas as pd

class ProfitStatic(Frame):
    def __init__(self, master):
        super().__init__(master)
        #coding:utf-8
        import matplotlib.pyplot as plt
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



    def test(self):
        df6 = ProfitTable().get_sorted_profit_group()
        legend = False
        names =  {'num':'item numbers', 'price_average': 'delivery price per package', 'tb_price':'total buy price', 'tc_price': 'total sell price', 'profit':'total profit'}
        for i, colName in enumerate(names.items()):
            print(colName)

            if i==0:
                legend = True
            else:
                legend = False
            self.plot_piechart(self.ax[i], df6,colName, legend)
            # self.plot_bar(self.ax[i], df6,colName)




    def plot_bar(self, ax, df):
        x = df['name']
        y = np.round(df[colName[0]],1)

        ax.bar(x, y)
        ax.set_title(colName[1])
        ax.set_xticklabels(labels = x, rotation = 90)
        for index, v in enumerate(y):
            ax.text(index, v, str(v))
        self.canvas.draw()


    def plot_piechart(self, ax, df, colName, legend = False):
        name = df['name']
        y = np.round(df[colName[0]],1)

        autopct='%1.1f%%'
        ax.pie(y,autopct=autopct)
        ax.set_title(colName[1])
        if legend:
            ax.legend(name).set_draggable(True)

        self.canvas.draw()








def main():
    root = Tk()
    app = ProfitStatic(root)
    app.pack(expand = True, fill = 'both')

    app.test()
    root.mainloop()

if __name__ == '__main__':
    main()
