import requests

class KechengAPi():

    def __init__(self, s, host="http://49.235.92.12:9000"):
        self.host = host
        self.s = s

    def login(self,
              username="test",
              password="123456"):
        '''登录获取token'''
        # s = requests.session()  # 会话  代码里面的浏览器，模拟浏览器的功能
        url = self.host+"/api/v1/login"
        body = {
            "username": username,
            "password": password
        }

        # 转json
        r = self.s.post(url, json=body)
        print(r.json())

        # token
        token = r.json()["token"]
        print("取出token:%s" % token)

        h = {
            "Authorization": "Token %s" % token
        }
        self.s.headers.update(h)  # 更新到session会话
        # 更新之后的头部
        return token

    def get_info(self):
        url = self.host+"/api/v1/userinfo"
        r = self.s.get(url)
        print(r.text)
        return r.json()
        # assert r.json()["msg"] == "sucess!"
        # assert r.json()["code"] == 0

    def updata_info(self,
                    name="test",
                    sex="M",
                    age=20,
                    mail="283340479@qq.com"):
        '''修改个人信息'''
        url = self.host+"/api/v1/userinfo"
        body = {"name": name,
                "sex": sex,
                "age": age,
                "mail": mail}
        r = self.s.post(url, json=body)
        print(r.text)
        return r.json()
        # assert r.json()["message"] == "update some data!"
        # assert r.json()["code"] == 0
        # assert r.json()["data"]["mail"] == "283340479@qq.com"


if __name__ == '__main__':
    pass
    # s = requests.session()
    # shili = KechengAPi(s)  # 实例化
    # shili.login(username="test2")        # 调用方法
    # shili.get_info()
    # shili.updata_info(name="test2")