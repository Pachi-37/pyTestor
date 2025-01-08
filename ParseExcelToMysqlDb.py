import os

import pandas as pd
import pymysql

from constant.MysqlSetting import MysqlSetting

xls = pd.ExcelFile('./resource/test.xlsx')
sheet_names = xls.sheet_names
df = xls.parse(sheet_name=sheet_names[0])
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

head = df.columns
db_name = sheet_names[0]

create_sql_template = f"CREATE TABLE  IF NOT EXISTS `{db_name}`("

columns_definition = []
for filed in head:
    if filed == "id":
        columns_definition.append(f"`{filed}` varchar(20) NOT NULL PRIMARY KEY")
    elif "need" in filed:
        columns_definition.append(f"`{filed}` tinyint(1) NOT NULL")
    elif "data" in filed:
        columns_definition.append(f"`{filed}` text NOT NULL")
    else:
        columns_definition.append(f"`{filed}` varchar(40) NOT NULL")

create_sql_template += ", ".join(columns_definition)
create_sql_template += ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

print(create_sql_template)

env_user = os.getenv(MysqlSetting.MYSQL_USER_ENV)
env_password = os.getenv(MysqlSetting.MYSQL_PASSWORD_ENV)
mysql_connect = pymysql.connect(host='localhost', port=3306, user=env_user, passwd=env_password, db='oa',
                                charset="utf8")
db_cursor = mysql_connect.cursor()
db_cursor.execute(create_sql_template)

db_cursor.execute(f"describe {db_name};")
for e in db_cursor.fetchall():
    print(e)

db_head = ["`{}`".format(item) for item in head]
insert_or_update_sql_template = f"INSERT INTO {db_name} ({','.join(db_head)}) VALUES (tmp_value) " \
                                f"ON DUPLICATE KEY UPDATE " \
                                f"{','.join([f'{col} = VALUES({col})' for col in db_head])};"

for index, row in df.iterrows():
    insert_or_update_sql = insert_or_update_sql_template.replace("tmp_value", ",".join("'{}'".format(item) for item in row))
    print(insert_or_update_sql)
    db_cursor.execute(insert_or_update_sql)
mysql_connect.commit()

db_cursor.execute(f"select * from {db_name}")
for e in db_cursor.fetchall():
    print(e)