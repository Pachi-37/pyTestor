import json

import pytest
import requests

from utils.mysql_utils import select_from_table
from utils.test_data_utils import TestInfo
import constant.AutoTestSetting as AutoTestConstant


@pytest.fixture(params=select_from_table('test_case', "request_module='购物车'"))
def get_test_data(request):
    return request.param


def test_cart(get_login_token, get_test_data):
    test_data = TestInfo(get_test_data)
    if test_data.need_login == 1:
        header = {
            "Jwt_token": get_login_token
        }
    else:
        header = {}

    if test_data.request_type == "get":
        if test_data.input_data == "nan":
            response = requests.get(AutoTestConstant.url + test_data.url, headers=header)
        else:
            response = requests.get(AutoTestConstant.url + test_data.url, headers=header, data=json.loads(test_data.input_data))
    else:
        if test_data.input_data == "nan":
            response = requests.post(AutoTestConstant.url + test_data.url, headers=header)
        else:
            response = requests.post(AutoTestConstant.url + test_data.url, headers=header, data=json.loads(test_data.input_data))

    assert 200 == response.status_code