import os

from constant.MysqlSetting import MysqlSetting

url = "http://127.0.0.1:8083"
env_user = os.getenv(MysqlSetting.MYSQL_USER_ENV)
env_password = os.getenv(MysqlSetting.MYSQL_PASSWORD_ENV)
login_data = {
    "userName": env_user,
    "password": env_password
}
