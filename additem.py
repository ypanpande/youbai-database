from datetime import date
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from youbai_database import Youbai_database

class Additem(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.t1 = ScrolledText(self)
        b1 = Button(self, text = 'parse', command = self.on_parse)
        self.t2 = ScrolledText(self, width = 50)
        b2 = Button(self, text = 'add item', command =self.on_additem)

        self.t1.grid(row = 0, column = 0, sticky = 'news')
        b1.grid(row = 1, column = 0)
        self.t2.grid(row = 0, column = 1, sticky = 'news')
        b2.grid(row = 1, column = 1)

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)



    def parse_copy(self, file):
        rownum = 0
        time = None
        package_num = None
        money = None
        start_goods = False
        goods = {}





                k = ''.join(f.split()[:-2])
                v = f.split()[-1]
                if k in goods.keys():
                    goods[k] += int(v)
                else:
                    goods[k] = int(v)
        return {'time':time, 'package_num':package_num, 'money':money, 'goods':goods}


    def on_additem(self):
        file = self.t1.get('1.0', 'end').strip()
        res = self.parse_copy(file)
        db = Youbai_database(self)

        for k, v in res['goods'].items():
             price_aver = round(float(res['money'])/float(len(res['goods'])),2)
             package_num_aver = round(float(res['package_num'])/float(len(res['goods'])),2)

             db.youbai_insert((k,v, res['time'],price_aver, package_num_aver))




    def on_parse(self):
        self.t2.delete('1.0', 'end')
        file = self.t1.get('1.0', 'end').strip()
        res = self.parse_copy(file)

        #add price..
        self.t2.insert('end', f'time: {res["time"]}'+'\n')
        self.t2.insert('end', f'package_num: {res["package_num"]}'+'\n')
        self.t2.insert('end', f'money: {res["money"]} Euro'+'\n\n')
        #add goods
        text = ''.join([f'{k}:{v}'+'\n' for k, v in res["goods"].items()])
        self.t2.insert('end', text)













def main():
    root = Tk()

    app = Additem( root)
    app.pack(expand = True, fill = 'both')
    root.mainloop()


if __name__=='__main__':
    main()
