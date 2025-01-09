import json

import pytest
import requests

from utils.mysql_utils import select_from_table, select_db_to_pd


class LoginInfo:
    def __init__(self, data_list):
        self.id = data_list[0]
        self.title = data_list[1]
        self.module = data_list[2]
        self.url = data_list[3]
        self.request_type = data_list[4]
        self.need_login = data_list[5]
        self.input_data = data_list[6]
        self.data_type = data_list[7]
        self.expect_result = data_list[8]
        self.response_code = None

        self.username = None
        self.password = None

        self._process_input_data()

    def _process_input_data(self):
        tmp_json_data = json.loads(self.input_data)
        self.username = tmp_json_data["userName"]
        self.password = tmp_json_data["password"]

        tmp_expect_json_data = json.loads(self.expect_result)
        self.response_code = int(tmp_expect_json_data["status"])


@pytest.fixture(params=select_from_table("test_case", "request_module='登录'"))
def get_login_data(request):
    """
    获取登录接口的测试数据
    :param request:
    :return:
    """
    login_data = request.param
    return login_data


@pytest.fixture(params=select_db_to_pd("test_case", "request_module='登录'"))
def get_login_data_pd(request):
    """
    获取登录接口的测试数据
    :param request:
    :return:
    """
    login_data = request.param
    return login_data


def test_login(get_login_data):
    login_info = LoginInfo(get_login_data)
    url = "http://127.0.0.1"
    if login_info.request_type == "get":
        response = requests.get(url + login_info.url, params=json.loads(login_info.input_data))
        assert response.status_code == 200
        assert json.loads(response.text).get("status") == login_info.response_code

    elif login_info.request_type == "post":
        response = requests.post(url + login_info.url, data=json.loads(login_info.input_data))
        assert response.status_code == 200
        assert json.loads(response.text).get("status") == login_info.response_code


def test_login_pd(get_login_data_pd):
    login_info = LoginInfo(get_login_data_pd)
    url = "http://127.0.0.1"
    if login_info.request_type == "get":
        response = requests.get(url + login_info.url, params=json.loads(login_info.input_data))
        assert response.status_code == 200
        assert response.status_code == login_info.response_code

    elif login_info.request_type == "post":
        response = requests.post(url + login_info.url, json=json.loads(login_info.input_data))
        assert response.status_code == login_info.response_code
