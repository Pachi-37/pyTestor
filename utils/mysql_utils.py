import os

import pandas as pd

from constant.MysqlSetting import MysqlSetting


def _get_mysql_connect():
    import pymysql
    env_user = os.getenv(MysqlSetting.MYSQL_USER_ENV)
    env_password = os.getenv(MysqlSetting.MYSQL_PASSWORD_ENV)
    db = {
        "host": "localhost",
        "port": 3306,
        "user": env_user,
        "passwd": env_password,
        "db": "mall",
        "charset": "utf8"
    }
    return pymysql.connect(**db)


def select_from_table(table_name, where_condition=None):
    connect = _get_mysql_connect()
    sql = "select * from %s" % table_name
    if where_condition is not None:
        sql += " where %s" % where_condition

    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def select_db_to_pd(table_name, where_condition=None):
    connect = _get_mysql_connect()
    sql = "select * from %s" % table_name
    if where_condition is not None:
        sql += " where %s" % where_condition

    result = pd.read_sql(sql, connect)
    res = []
    for index, row in result.iterrows():
        tmp = []
        for col in result.columns:
            tmp.append(row[col])
        res.append(tmp)
    return res

