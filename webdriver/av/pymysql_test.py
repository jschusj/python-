import pymysql

# http://www.runoob.com/python3/python3-mysql.html

# 打开数据库连接
db = pymysql.connect("localhost", "root", "Yang163110", "tianba")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO javmost(series, `name`, title, img_url, play_url) 
        VALUES ('SDDE', 'SDDE-419', 'fuck av', 'www.img', 'www.play')"""

try:
    # 执行sql语句
    result = cursor.execute(('SELECT COUNT(*) FROM javmost where `name`="%s"') % ('WANZ-232'))
    tuple_count = cursor.fetchall()[0]
    count = tuple_count[0]
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as err:
    # 如果发生错误则回滚
    print(err)
    db.rollback()

# 关闭数据库连接
db.close()
