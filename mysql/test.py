import pymysql
# 打开数据库
db = pymysql.connect(host='127.0.0.1', user='root', password='lisent', database='test', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

def insert(_date,_money,_polt,_type,_way,_info):
    year,mnoth,day = _date.split('-')
    sql = "insert into buy_info(year,month,day,money,polt,type,way,info) values((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
    cursor.execute(sql,[year,mnoth,day,_money,_polt,_type,_way,_info])
    db.commit()
    return cursor.rowcount


file_path = "/home/lisent/codes/python/GUI/temp1"
with open(file_path, encoding='utf-8') as file_obj:
	lines = file_obj.readlines()
for line in lines:
	date,money,polt,type,way,info = line.split(",")
	insert(date,money,polt,type,way,info)
