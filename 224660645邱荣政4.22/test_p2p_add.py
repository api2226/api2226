import unittest,requests
from db import *

class MyTestCase(unittest.TestCase):
    url = "http://192.168.55.51:8080/p2p_management/addProduct"
    header = {
        "Content-Type: application/x-www-form-urlencoded"
    }
    def test_add_ok(self,noname):
        if check_user(noname):
            del_user(noname)
        data = {"proNum":"001","proName":"月季","proLimit":"54","annualized":"70"}
        r = requests.post(url=self.url, headers=self.header, json=data)
        self.assertIn("成功", r.text)
    def test_add_err(self,name):
        if not check_user(name):
            add_user(name)
        data={"proNum":"001","proName":"月季","proLimit":"54","annualized":"70"}
        r = requests.post(url=self.url,json=data)
        result={"code":2,"message":"用户已存在","response":None}
        self.assertDictEqual(result,r.json())



if __name__ == '__main__':
    unittest.main()
