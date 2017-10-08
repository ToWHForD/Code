# -*- coding: utf-8 -*- 
"""
描述:实现自动化登录百度贴吧并进行签到操作
原理：通过对百度贴吧签到抓包的发现，签到的实际操作是登陆后向网站发送
    一个post请求，该请求包含三个值，编码集，贴吧名和tbs值，前两者固定，
    唯一需要获取的就是tbs值，而tbs值，同时也可以由get方法向网站请求获取
    到值。
"""
import requests
from config import *
class checkIn:
    def __init__(self,tieba_list):
        self.tieba_list = tieba_list
        self.tbs_url='http://tieba.baidu.com/dc/common/tbs'
    def get_tbs(self):
        try:
            tbs_dic = eval(requests.get(self.tbs_url).text) #将字符串转换为字典
            tbs_value = tbs_dic['tbs']          
        except Exception as e:
            print("获取tbs值失败，请稍后重试~~")
            tbs_value = None
        #print("tbs的值为：",tbs_value)    
        return tbs_value
    def check(self,name):
        baidu_url = 'http://tieba.baidu.com/sign/add'
        data={
            'ie':'utf-8',
            'kw':name,
            'tbs':checkIn.get_tbs(self)
            }
        try:
            requests.request("post",baidu_url,cookies = tieba_cookies,data = data)
            print("%s吧已经签到！"%name)
        except:
            print("签到%s失败"%name)

    def sign(self):
        for name in self.tieba_list:
            checkIn.check(self,name)

#cookies重要的是BDUSS的值，这个值是百度用户登录的唯一凭证。
#签到是向baidu_url post一个data数据包，这个数据包是个由ie，kw和tbs组成的
#tbs的值是变化的，但可以通过向tbs_url执行get请求得到这个值
def main():
    tieba_list = ["王维","we","朱淑真"]
    card = checkIn(tieba_list)
    card.sign()
    
if __name__ == '__main__':
    main()
