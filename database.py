import pymysql
import tkinter as tk

# 打开数据库
db = pymysql.connect(host='127.0.0.1', user='root', password='lisent', database='test', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


def Query():
    sql = "select * from buy_info;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result

def query(key,value):
    temp = "id,year,month,day,money,polt,type,way"
    if key == "年":
        sql = "select "+temp+" from buy_info where year = %s;"
    elif key == "月":
        sql = "select "+temp+" from buy_info where month = %s;"
    elif key == "日":
        sql = "select "+temp+" from buy_info where day = %s;"
    elif key == "金额":
        sql = "select "+temp+" from buy_info where money = %s;"
    elif key == "平台":
        sql = "select "+temp+" from buy_info where polt = %s;"
    elif key == "商品类型":
        sql = "select "+temp+" from buy_info where type = %s;"
    elif key == "支付方式":
        sql = "select "+temp+" from buy_info where way = %s;"
    else:
        return 
    cursor.execute(sql,value)
    result = cursor.fetchall()
    # print(result)
    return result

def insert(_date,_money,_polt,_type,_way,_info):
    year,mnoth,day = _date.split('-')
    sql = "insert into buy_info(year,month,day,money,polt,type,way,info) values((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
    cursor.execute(sql,[year,mnoth,day,_money,_polt,_type,_way,_info])
    db.commit()
    return cursor.rowcount

def delete(id):
    sql = "delete from buy_info where id = %s"
    cursor.execute(sql,id)
    db.commit()
    return cursor.rowcount

def update(id,key,value):
    id = int(id)
    # print(type(id))
    sql = "update buy_info set %s"%(key)+"= %s where id = %s"
    cursor.execute(sql,[value,id])
    db.commit()
    return cursor.rowcount

if __name__ == '__main__':
    print ("2020-12-3".split('-'))