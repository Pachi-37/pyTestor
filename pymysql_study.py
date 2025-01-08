import os

import pymysql

from constant.MysqlSetting import MysqlSetting
from utils.SqlUtils import SqlUtils

env_user = os.getenv(MysqlSetting.MYSQL_USER_ENV)
env_password = os.getenv(MysqlSetting.MYSQL_PASSWORD_ENV)
conn = pymysql.connect(host='localhost', port=3306, user=env_user, passwd=env_password, db='oa',charset="utf8")

cursor = conn.cursor()
sql_statements = SqlUtils.read_sql_file("sql/oa.sql")
for statement in sql_statements:
    cursor.execute(statement)
conn.commit()
cursor.execute("select * from sys_role")
print(cursor.fetchall())
