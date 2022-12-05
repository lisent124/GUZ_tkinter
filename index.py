
from tkinter import *
import tkinter as tk
from tkinter import ttk
from database import *





def addData():
    root = Tk()
    root.title('添加数据')
    Label(root, text='时间:').grid(row=0)
    Label(root, text='金额:').grid(row=1)
    Label(root, text='平台:').grid(row=2)
    Label(root, text='商品种类:').grid(row=3)
    Label(root, text='支付方式:').grid(row=4)
    Label(root, text='备注:').grid(row=5)

    _date = Entry(root, textvariable=StringVar())
    _money = Entry(root, textvariable=StringVar())
    _polt = Entry(root, textvariable=StringVar())
    _type = Entry(root, textvariable=StringVar())
    _way = Entry(root, textvariable=StringVar())
    _info = Entry(root, textvariable=StringVar())

    _date.grid(row=0, column=1, padx=10, pady=10)
    _money.grid(row=1, column=1, padx=10, pady=5)
    _polt.grid(row=2, column=1, padx=10, pady=5)
    _type.grid(row=3, column=1, padx=10, pady=5)
    _way.grid(row=4, column=1, padx=10, pady=5)
    _info.grid(row=5, column=1, padx=10, pady=5)

    def add_data():
        if _date == "":
            tk.messagebox.showerror('提示', '请输入日期,如:2020-12-1')
            return
        result = insert(_date.get(),_money.get(),_polt.get(),_type.get(),_way.get(),_info.get())
        if result:
            print('添加成功')
            tk.messagebox.showinfo('提示', '添加成功!')
        else:
            print('添加失败')
            tk.messagebox.showerror('提示', '添加失败!')

    Button(root, text='添加', width=10, command=add_data).grid(row=7, column=4, sticky=W, padx=10, pady=5)

    root.mainloop()


def updateData():
    root = Tk()
    root.title('修改数据')
    Label(root,text="交易编号：").grid(row=0)
    Label(root, text='金额:').grid(row=2)
    Label(root, text='平台:').grid(row=3)
    Label(root, text='商品种类:').grid(row=4)
    Label(root, text='支付方式:').grid(row=5)

    _id = Entry(root,textvariable=StringVar())
    _money = Entry(root, textvariable=StringVar())
    _polt = Entry(root, textvariable=StringVar())
    _type = Entry(root, textvariable=StringVar())
    _way = Entry(root, textvariable=StringVar())

    _id.grid(row=0, column=1, padx=10, pady=10)
    _money.grid(row=2, column=1, padx=10, pady=5)
    _polt.grid(row=3, column=1, padx=10, pady=5)
    _type.grid(row=4, column=1, padx=10, pady=5)
    _way.grid(row=5, column=1, padx=10, pady=5)

    def update_data():
        result = 1
        if _id.get() == "":
            tk.messagebox.showinfo('提示', '请输入交易编号!')
            return
        if _money.get():
            result *= update(_id.get(),"money",_money.get())
        if _polt.get():
            result *= update(_id.get(),"polt",_polt.get())
        if _type.get():
            result *= update(_id.get(),"type",_type.get())
        if _way.get():
            result *= update(_id.get(),"way",_way.get())
        if result:
            print('更新成功')
            tk.messagebox.showinfo('提示', '更新成功!')
        else:
            print('更新失败')
            tk.messagebox.showerror('提示', '更新失败!')

    Label(root,text="空 即不修改").grid(row=7)
    Button(root, text='修改', width=10, command=update_data).grid(row=8, column=4, sticky=W, padx=10, pady=5)

    root.mainloop()


def deleteData():
    root = Tk()
    root.title('修改数据')
    Label(root,text="交易编号：").grid(row=0)
    _id = Entry(root,textvariable=StringVar())

    _id.grid(row=0, column=1, padx=10, pady=10)

    def delete_data():
        result = delete(_id.get())
        if result:
            print('删除成功')
            tk.messagebox.showinfo('提示', '删除成功!')
        else:
            print('删除失败')
            tk.messagebox.showerror('提示', '删除失败!')

    Button(root, text='修改', width=10, command=delete_data).grid(row=8, column=4, sticky=W, padx=10, pady=5)

    root.mainloop()