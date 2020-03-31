import requests
from ke13.login_class import KechengAPi
import pytest

@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    shili = KechengAPi(s)  # 实例化
    shili.login()        # 调用方法
    return shili


def test_get_info(login_fixture):
    res = login_fixture.get_info()
    assert res["msg"] == "sucess!"
    assert res["code"] == 0

