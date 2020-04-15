import requests
from ke13.login_class import KechengAPi
import pytest
import allure
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


@allure.title("aaaaaaaeeeeeee")
def test_4111():
    print("啦啦啦啦")


# '''
# pytest --alluredir ./report/allure_raw
#
# pytest --alluredir ./report/allure_raw --allure-epics=epic
#
# allure serve report/allure_raw
#allure serve ./all1
#
# allure对用例的等级划分成五个等级
#  blocker　 阻塞缺陷（功能未实现，无法下一步）
#  critical　　严重缺陷（功能点缺失）
#  normal　　 一般缺陷（边界情况，格式错误）
#  minor　 次要缺陷（界面错误与ui需求不符）
#  trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
#
# '''