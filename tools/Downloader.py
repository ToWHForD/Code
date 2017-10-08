#encoding=UTF-8
import requests
import re

#google的chrome浏览器的标识
agent="Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36"

class Download:
    @staticmethod
    def getHttpStatus(url,redict=False):
        try:
            return requests.get(url,allow_redirects=redict).status_code

        except Exception as e:
            print("哎呀出错了呢，可能是网络的问题，检查下网络吧！",e) 
            return None

    @staticmethod
    def getHttpSource(url,retry_time=3,user_agent=agent,charset='UTF-8'):
        headers = {"user_agent":agent}
        req = requests.get(url,headers=headers,allow_redirects=False)
        req.encoding = charset
        status=Download.getHttpStatus(url)
        try:
            if status == None:
                pass    
            elif status >= 500:
                if retry_time>0:
                    print("正在尝试重新下载，剩余重试%s次"%(retry_time-1))
                    return Download.getHttpSource(url,retry_time-1)
            elif status >= 400:
                print("网页找不到了~~")
            elif status >= 300:
                print("该网页或许已经被重定向了~~")
            html = None
            if status == 200:
                html = req.text
            return html
        
        except Exception as e :
            print("我也不知道出了什么错误辣~仔细看看错误信息吧~~")
            print(e)
            return None

    @staticmethod
    def matchList(re_value,url):
        html = Download.getHttpSource(url)
        if html != None:
            try:
                mList = re.findall(re_value,html)
            except Exception as e:
                print(e)
                mList = []

        return mList

