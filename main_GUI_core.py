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
        b1 = Button(f1, text = 'ok', command = self.on_ok_date)





        #text inf
        f2 = Frame(self)
        self.inf = ScrolledText(f2, height = 10, width = 120)
        self.inf.pack(expand = True, fill = 'both')
        self.update_inf(data) # write informaion to text panel

        #table
        f3 = Frame(self)

        self.tb = Table(f3, dataframe = data['df'], height = 600)
        self.tb.show()

        f_top.pack(expand = True, fill = 'both')
        f2.pack(expand = True, fill = 'both')
        f3.pack(expand = True, fill = 'both')

        self.e1.insert('end', '2021-08-01')
        self.e2.insert('end', date.today())



    def on_ok_date(self):
        #1. inf
        start = self.e1.get()
        end = self.e2.get()
        data = ProfitTable().get_all_data(start = start, end = end)
        self.update_inf(data)
        #2. table
        self.tb.model.df = data['df']
        self.tb.redraw()


    def update_inf(self, data):

        #1. text inf
        tprice = round(data["tprice"], 2)
        num = round(data["tpackage_num"])
        tb_price = round(data['tb_price'], 2)
        tc_price = round(data['tc_price'], 2)
        profit = round(data['profit'], 2)

        text = []
        text.append(f'delivery price: {tprice}')
        text.append(f'package num: {num}')
        text.append(f'tb_price: {tb_price}')
        text.append(f'tc_price: {tc_price}')
        text.append(f'profit: {profit}')

        self.inf.delete('1.0', 'end')
        self.inf.insert('end', ''.join([t+'\n' for t in text]))


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
