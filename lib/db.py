import pymysql


def get_db_conn():
    conn = pymysql.connect(
        # host='rm-drdshhid01h4s10rpublic.drds.aliyuncs.com', #订单+用户
        host='rm-wz91id26pzz91t02gqo.mysql.rds.aliyuncs.com',  # 药店药品库
        port=3306,
        user='u_hwydy_dev',
        password='Ydy123456dev',
        # db='hw_ydy_user_dev',
        db='hw_ydy_drugstore_dev',
        charset='utf8'
    )
    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()
    cursor = conn.cursor()
    result = cursor.execute(sql)
    cursor.close()
    conn.close()
    return result


# 封装数据库修改操作
def update_db(sql):
    conn = get_db_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接


# 封装常用数据库操作

# 查询门店下药品
def query_drug(store_no, status):
    sql = "select * from qyw_shop_drugs where store_no='{}' and status={}".format(store_no, status)
    result = query_db(sql)
    return True if result else False
