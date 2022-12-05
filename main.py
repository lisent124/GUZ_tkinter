
from tkinter import *
import tkinter as tk
from tkinter import ttk
from database import *
from index import *
import tkinter.messagebox  as tmb# 消息框

root = tk.Tk()
root.title("帐务管理系统")
root.geometry("650x300")

def show_data():
    text.delete('1.0', 'end')  # 从第一行开始，全部删除
    key = cbox.get()
    value = seek_by.get()

    if value == None:
        tmb.showinfo('提示', '请输入查询信息')  
        return

    list = query(key=key,value=value)

    if list == None:
        tmb.showinfo('提示', '无结果')  
        return

    title = ['交易编号','年','月','日','金额','平台','商品种类','支付方式','备注']
    for i in title:
        text.insert(INSERT,"%-4s "%i)
    text.insert(INSERT,"\n")
    for i in list:
        for key, value in i.items():
            text.insert(INSERT,"%-5s "%value)
        text.insert(INSERT,"\n")

    tmb.showinfo('提示', '查询成功!')
    
    pass


f1 = Frame(root)
tk.Label(f1,text="lisent").grid(row=0,column=0)
tk.Button(f1, text="修改数据",command=updateData).grid(row=0,column=1)
tk.Button(f1,text="添加数据",command=addData).grid(row=0,column=2)
tk.Button(f1,text="删除数据",command=deleteData).grid(row=0,column=3)

cbox = ttk.Combobox(f1)
cbox.grid(row=1)
cbox['value'] = ('年','月','日','金额','平台','商品种类','备注')
#通过 current() 设置下拉菜单选项的默认值# print(cbox.get())
cbox.current(0)

seek_by = Entry(root, textvariable=StringVar())
# seek_by.
seek_by.place(x=180,y=35,width=150)

tk.Button(f1,text="查看数据",command=show_data).grid(row=1,column=4)


f1.place(x=0,y=0)


f2 = Frame(root)
text = tk.Text(f2)
text.grid(row=1,column=1)
f2.place(x=0,y=80)


root.mainloop()

