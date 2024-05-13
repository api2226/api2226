import unittest
from xzs.business.xzs_login import xzs_login


class MyTestCase(unittest.TestCase):
    x = xzs_login()
    def test_login_ok(self):
        t = self.x.login(
            data={"userName":"去看看","password":"123456","remember":False}
        )
        self.assertIn("成功",t)

    def test_login_err(self):
        t = self.x.login(
            data={"userName": "", "password": "123456", "remember":False}
        )
        self.assertIn("用户名或密码错误", t)


if __name__ == '__main__':
    unittest.main()
