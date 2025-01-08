import os

import pytest

from constant.MysqlSetting import MysqlSetting


def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

# python 3.6 使用 setup() teardown()，新版方法里面优先级下降

@pytest.mark.trylast
def test_demo():
    assert 2 == 1


@pytest.mark.parametrize("a,b,c", [(1, 2, 3), (4, 5, 9)])
def test_add(a, b, c):
    assert a + b == c


import pymysql

env_user = os.getenv(MysqlSetting.MYSQL_USER_ENV)
env_password = os.getenv(MysqlSetting.MYSQL_PASSWORD_ENV)
conn = pymysql.connect(host='localhost', port=3306, user=env_user, passwd=env_password, db='oa', charset="utf8")

cursor = conn.cursor()
cursor.execute(r"select * from `test_case`")
result = cursor.fetchall()


@pytest.mark.run(order=1)
@pytest.mark.parametrize(["id", "name", "module", "url", "method", "status", "data", "style", "expect"], result)
def test_mysql_result(id, name, module, url, method, status, data, style, expect):
    print(module)
