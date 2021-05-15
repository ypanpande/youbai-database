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


    # get grouped profit table
    def create_profit_table_group(self, start = '2021-08-01', end = date.today() ):
        price_df = pd.read_sql_query('SELECT * FROM product_price', sqlite3.connect('youbai.db'))
        sql = f'SELECT * FROM goods WHERE day BETWEEN "{start}" AND "{end}"'
        goods_df = self.create_goods_table_group(start, end)

        tem = []
        for index1, row in goods_df.iterrows():
            name = row['name']
            num = row['num']
            choose_item = price_df[price_df['name'] == name].to_numpy()

            buy_price = float(choose_item[0][1])
            sell_price = float(choose_item[0][2])

            tem.append({'name': name, 'num':num, 'price_average': row['price_average'], 'package_num_average':row['package_num_average'], 'tb_price': buy_price*float(num), 'tc_price' :sell_price*float(num), 'profit':  sell_price*float(num)-buy_price*float(num)})

        return pd.DataFrame(tem)

    # get grouped goods table
    def create_goods_table_group(self, start = '2021-08-01', end = date.today()):
        sql = f'SELECT * FROM goods WHERE day BETWEEN "{start}" AND "{end}"'
        goods_df = pd.read_sql_query(sql, sqlite3.connect('youbai.db'))

        tem = []
        for index1, row in goods_df.iterrows():
            name = row['name']
            num = float(row['num'])
            price_average = float(row['price_average'])
            package_num_average = float(row['package_num_average'])
            lname = [v['name'] for v in tem]
            if name in lname:
                i = lname.index(name)
                tem[i]['num'] += num
                tem[i]['price_average'] += price_average
                tem[i]['package_num_average'] += package_num_average
            else:
                ele = {'name':name,'num':num, 'price_average':price_average, 'package_num_average':package_num_average }
                tem.append(ele)

        return pd.DataFrame(tem)

        # get first 5 rows from grouped profit table
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
