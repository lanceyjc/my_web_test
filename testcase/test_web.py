# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.searchPage import SearchPage
import time
import unittest
from page.searchPage import *
from common.screenShot import ScreenShot


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        # self.driver = webdriver.Firefox()
        self.url = SearchPage.url
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.page = SearchPage(self.driver)
        self.page.get(self.url)

    def tearDown(self):
        self.driver.close()

    def test_login_success(self):
        # 使用pageObject模式时的web页面自动化测试代码
        self.page.login.click()
        self.page.user_name = self.page.name_content
        self.page.user_pw = self.page.pw_content
        self.page.login_btn.click()
        login_name = self.page.login_name.text
        time.sleep(2)
        # 断言
        try:
            self.assertIn(self.page.login_name_content_assert, login_name)
        except AssertionError:
            ScreenShot(self.driver).screen_shot()
            raise AssertionError

        # # 未使用pageObject模式时的web页面自动化测试代码
        # self.driver.find_element_by_id("kw").send_keys("hello")
        # self.driver.find_element_by_id("su").click()
        # time.sleep(2)
        # self.assertIn("hello", self.driver.page_source)

    def test_login_fail(self):
        # 错误的断言导致测试用例failed
        self.page.login.click()
        self.page.user_name = self.page.name_content_wrong
        self.page.user_pw = self.page.pw_content_wrong
        self.page.login_btn.click()
        alert_content = self.page.alert.text
        time.sleep(2)
        try:
            self.assertIn(self.page.login_fail_content_assert, alert_content)
        except AssertionError:
            ScreenShot(self.driver).screen_shot()
            raise AssertionError

        # # 未使用pageObject模式的web页面自动化测试代码
        # self.driver.find_element_by_id("kw").send_keys("hello")
        # self.driver.find_element_by_id("su").click()
        # time.sleep(2)
        # self.assertIn("hello1232323", self.driver.page_source)

    # def test_search2(self):
    #     # 元素值错误，导致的自动化测试用例error
    #     self.page.wrong_search = self.page.search_content
    #     self.page.search_btn.click()
    #     time.sleep(2)
    #     self.assertIn(self.page.search_content_assert, self.driver.page_source)

        # # 未使用pageObject模式的web页面自动化测试代码
        # self.driver.find_element_by_id("k").send_keys("hello")
        # self.driver.find_element_by_id("su").click()
        # time.sleep(2)
        # self.assertIn("hello", self.driver.page_source)


if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    # now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin("test_search"))
    # suite.addTest(TestLogin("test_search1"))
    # suite.addTest(TestLogin("test_search2"))
    # path = "../report/" + now + "result.html"
    # fp = open(path, 'wb')
    #
    # runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试查询功能")
    # runner.run(suite)
    # fp.close()
    unittest.main()

