from common.pageObject import PageObject, PageElement
from common.url import *


class SearchPage(PageObject):

    # 当前测试页面的测试网址url
    base_url = Url.base_url
    url = base_url+'/'

    # 查询元素
    # search = PageElement(id="kw")
    # wrong_search = PageElement(id="k")
    # search_btn = PageElement(id='su')
    login = PageElement(css="a[title='登录']")
    user_name = PageElement(name="user_name")
    user_pw = PageElement(name="user_pw")
    login_btn = PageElement(class_name="loginbtn1")
    alert = PageElement(css=".layui-layer-content")
    login_name = PageElement(css="a[href='http://www.phpshe.com/demo/phpshe/user.php']")



    # 查询内容
    name_content = "lance"
    name_content_wrong = "lancer"
    pw_content = "123456"
    pw_content_wrong = "1234567"

    # 断言
    login_name_content_assert = "lance"
    login_name_content_assert_wrong = "hello12232423423"
    login_fail_content_assert = "帐号或密码错误"
    login_fail_content_assert_wrong = "登录成功"
    name_empty_content_assert = "请填写帐号"
    pw_empty_content_assert = "请填写密码"
