import sqlite3
import pandas as pd
from tkinter import *
from tkinter import messagebox
from pandastable import Table
import numpy as np

class Youbai_database(Frame):
    def __init__(self, master):
        super().__init__(master)
        # self.master = master

        f = Frame(self)# table
        b = Button(self, text = 'save table', command = self.on_save_table)# button

        f.pack()
        b.pack()
        ugoods = self.get_all_data()['ugoods']

        ugoods_df = pd.DataFrame(ugoods.items(), columns = ['name', 'count'])
        ugoods_df['buy_price'] = ''
        ugoods_df['sell_price'] = ''

        self.tb = Table(f, dataframe = ugoods_df,showtoolbar=True, showstatusbar=True, editable = True)
        self.tb.show()

        con = sqlite3.connect('youbai.db')
        cursor = con.cursor()
        query = 'CREATE TABLE IF NOT EXISTS product_price(name TEXT, buy_price TEXT, sell_price TEXT)'
        cursor.execute(query)
        con.commit()
        con.close()





    def on_save_table(self):
        df = self.tb.model.df
        con = sqlite3.connect('youbai.db')

        df.to_sql('product_price', con, if_exists = 'replace', index = False)












    def get_all_data(self):
        df = self.youbai_search()


        return {'ugoods': ugoods, 'tprice': tprice, 'tpackage_num': tpackage_num }







    def youbai_create(self):
        con = sqlite3.connect('youbai.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE goods(name TEXT, num TEXT, day TEXT, price_average TEXT, package_num_average TEXT)')
        con.commit()
        con.close()

    def youbai_insert(self, entities):
        try:
            con = sqlite3.connect('youbai.db')
            cursor = con.cursor()
            cursor.execute('INSERT INTO goods VALUES (?, ?, ?, ?,?)', entities)
        except:
            messagebox.showerror(title = 'add fail', message = sqlite3.Error)
        finally:
            con.commit()
            con.close()

    def youbai_search(self):
        con = sqlite3.connect('youbai.db')
        cursor = con.cursor()
        re = cursor.execute('SELECT * from goods')
        rows = re.fetchall()
        column = [s[0] for s in re.description]

        df = pd.DataFrame(data = rows, columns = column)



        con.commit()
        con.close()

        return df




def main():
    root = Tk()
    app = Youbai_database(root)
    app.pack()
    root.mainloop()

if __name__=='__main__':
    main()
