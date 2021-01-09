import requests


def getResp():
    r = requests.get('http://www.baidu.com')
    print(r.text)


if __name__ == '__main__':
    getResp()
else:
    print("http_request模块初始化")
