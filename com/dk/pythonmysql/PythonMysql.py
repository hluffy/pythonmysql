import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='mydata')

cursor = conn.cursor()

data = [
    ('han','han','M'),
    ('han1','han1','M')
]

# 插入数据
# effect_row = cursor.executemany('insert into student(name,password,gender) values(%s,%s,%s)',data)
# conn.commit()
# print(effect_row)
# print(cursor.lastrowid)

# 查询数据
effect_row = cursor.execute('select * from student')
# print(cursor.fetchall())
# print(cursor.fetchone())
print(cursor.fetchmany(3))

cursor.close()
conn.close()