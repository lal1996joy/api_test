import pymysql
from config.config import *


class DBUSER:

    def __init__(self):
        self.conn = pymysql.connect(
            host='drdshhid01h4s10rpublic.drds.aliyuncs.com',  # 订单+用户
            port=3306,
            user='u_hwydy_dev',
            password='Ydy123456dev',
            db='hw_ydy_user_dev',
            charset='utf8'
        )

        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 封装数据库查询操作
    def query(self, sql):
        logging.debug(sql)  # 输出执行的sql
        result = self.cursor.execute(sql)
        logging.debug(self.cursor.fetchall())       # 输出查询结果
        return result

    # 封装数据库修改操作
    def update(self, sql):
        # logging.debug(sql)      # 输出执行的sql
        try:
            self.cursor.execute(sql)  # 执行sql
            self.conn.commit()  # 提交更改
        except Exception as e:
            self.conn.rollback()  # 回滚
            # print(str(e))
            logging.error(str(e))       # 输出错误信息
    # 封装常用数据库操作

    # 查询用户是否存在
    def query_user(self, account):
        sql = "select * from qyw_users where account = '{}'".format(account)
        result = self.query(sql)
        return True if result else False  # 返回True或False

    # 删除用户
    def del_user(self, account):
        sql = "delete from qyw_users where account = '{}'".format(account)
        self.update(sql)
