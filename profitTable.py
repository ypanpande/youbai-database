import sqlite3
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import pandas as pd
from pandastable import Table
import numpy as np
from datetime import date

class ProfitTable():

    # get profit table





    def get_sorted_profit_group(self, start = '2021-08-01', end = date.today()):

        df = self.create_profit_table_group().sort_values('profit', ascending = False)

        df5 = df.iloc[:5]
        name = 'others'
        num = np.sum(df.iloc[5:]['num'])
        price_average = np.sum(df.iloc[5:]['price_average'])
        package_num_average = np.sum(df.iloc[5:]['package_num_average'])
        tb_price = np.sum(df.iloc[5:]['tb_price'])
        tc_price = np.sum(df.iloc[5:]['tc_price'])
        profit = np.sum(df.iloc[5:]['profit'])

        rest_row = pd.DataFrame(data = [{'name':name, 'num':num, 'price_average':price_average, 'package_num_average':package_num_average, 'tb_price':tb_price, 'tc_price':tc_price, 'profit':profit}])

        df6 = pd.concat([df5, rest_row])
        return df6







def main():
    root = Tk()
    f = Frame(root)
    f.pack()

    df = ProfitTable().create_profit_table()
    txt = Table(f, dataframe = df)
    txt.show()

    root.mainloop()


if __name__ == '__main__':
    main()
