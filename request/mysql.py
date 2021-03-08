import pymysql

# 1.建立连接
conn = pymysql.connect(
    host='drdshhid01h4s10rpublic.drds.aliyuncs.com',    #主机
    port=3306,  #端口
    user='u_hwydy_dev', #用户名
    password='Ydy123456dev',    #密码
    db='hw_ydy_user_dev'    #数据库
)

# 2.从连接建立游标（有游标才能操作数据库）
cur = conn.cursor()

# 3.查询（读）
cur.execute("select id,account from qyw_users where account = '18245284815'")

# 4.获取查询结果
# 需要重复使用查询结果时，需要将查询结果赋给某个变量
result = cur.fetchall()
print(result)   #((4803015, '18245284815'),)
print(result)   #((4803015, '18245284815'),)

# 获取完数据后，数据会从数据集中删除，再次获取获取不到
print(cur.fetchone())   #None
print(cur.fetchall())   #()

cur.close()
conn.close()