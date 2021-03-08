import pymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            # host='rm-drdshhid01h4s10rpublic.drds.aliyuncs.com', #订单+用户
            host='rm-wz91id26pzz91t02gqo.mysql.rds.aliyuncs.com',  # 药店药品库
            port=3306,
            user='u_hwydy_dev',
            password='Ydy123456dev',
            # db='hw_ydy_user_dev',
            db='hw_ydy_drugstore_dev',
            charset='utf8'
        )

        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 封装数据库查询操作
    def query(self, sql):
        result = self.cursor.execute(sql)
        return result

    # 封装数据库修改操作
    def update_db(self, sql):
        try:
            self.cursor.execute(sql)  # 执行sql
            self.conn.commit()  # 提交更改
        except Exception as e:
            self.conn.rollback()  # 回滚
            print(str(e))

    # 封装常用数据库操作

    # 查询门店下药品
    def query_drug(self, store_no, status):
        sql = "select * from qyw_shop_drugs where store_no='{}' and status={}".format(store_no, status)
        result = self.query(sql)
        # return True if result else False
        return self.cursor.fetchall()

