import time
import yaml
from BaseApp import BasePage
from testpage import Operations

with open("C:/Users/alexa/OneDrive/Рабочий стол/PageObject3/Seminar3/testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
passwd = testdata["password"]

def test_step1(er1, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login()
    page.enter_pass()
    page.click_login_button()
    
    assert page.get_error_text() == er1
  

# def test_step2(x_selector1, x_selector2, x_selector3, x_selector4, btn_selector, er2, browser):
#     site = BasePage(browser)
#     input1 = site.find_element(x_selector1)
#     input1.clear()
#     input1.send_keys(name)
#     input2 = site.find_element(x_selector2)
#     input2.clear()
#     input2.send_keys(passwd)
#     btn = site.find_element(btn_selector)
#     btn.click()
#     user_label = site.find_element(x_selector3)
#     text = user_label.text
#     assert text == er2