
quanju = 100

class Father():

    def fangzi(self):
        print("父亲的房子")

    def __fangzi1(self):
        print("父亲留给私生子的房子")

    def __fangzi2(self):
        print("父亲留给私生子父亲的房子")


class Mother():

    def chezi(self):
        print("母亲的车子")




class DuiXiang(Father, Mother):

    class_quanju = 200

    def __init__(self, age=18):
        shengxiao = "猴"  # 局部变量
        self.age = age    # 加了self,class 里面全局生效
        self.name = "对象"
        self.fan = "吃火锅"
        print(quanju)
        # self.chi = self.chifan()   # 属性里面调用方法

    # def 叫方法
    def kandianying(self):
        print("看电影的时候，未满18不让入场：%s"% self.age)
        print("和你的对象看电影")
        print(quanju)
        print(self.class_quanju)

    def chifan(self):
        print("吃饭")
        return "返回吃饭"

    def dayouxi(self):
        print("吃饭的内容：%s"% self.fan)
        a = "王者荣耀"
        print("打游戏：%s"%a)

    def shengxiaohai(self):
        return "小孩"

    def fangzi(self):
        # 方法的重写
        print("重新装修你父亲的房子，变成自己的了")


# 创建对象的实例

# __init__ 里面 的内容，自动先执行
nvpengyou = DuiXiang(age=28)  # 实例
nvpengyou.kandianying()
nvpengyou.fangzi()
nvpengyou.chezi()


# nvpengyou.dayouxi()
# nvpengyou.tui = "大长腿"
#
#
# print(nvpengyou.tui)
#


# print(nvpengyou.chi)
# print(nvpengyou.chi)
# print(nvpengyou.chifan())



# print(nvpengyou.age)    # 属性
# print(nvpengyou.name)   # 属性
#
# # 行为  方法
# nvpengyou.kandianying()
# nvpengyou.chifan()
# nvpengyou.dayouxi()
#
# a = nvpengyou.shengxiaohai()
# print(a)


