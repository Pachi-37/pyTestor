import json

import pytest
import requests

import constant.AutoTestSetting as AutoConstant


@pytest.fixture(scope="session", autouse=True)
def get_login_token():
    login_uri = "/loginWithJwt"
    login_response = requests.get(AutoConstant.url + login_uri, AutoConstant.login_data)
    assert 200 == login_response.status_code
    return json.loads(login_response.text)["data"]
