#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

USER = ''
PASSWD = ''

LOGIN_URL = 'http://web.oa.zulong.com/C6/JHSoft.Web.Login/OALogin.aspx'
INDEX_URL = 'http://web.oa.zulong.com/C6/jhsoft.web.portal/default/index.aspx'

browser = None

def login(user, password):
    browser.get(LOGIN_URL)
    browser.find_element_by_id("login_user").send_keys(user)
    browser.find_element_by_id("login_pswd").send_keys(password)
    browser.find_element_by_id("login_btn").click()
    WebDriverWait(browser, 3)

def checkout():
    browser.execute_script("DoSignOutCheck();")
    WebDriverWait(browser, 3).until(
        lambda x: x.find_element_by_class_name('signOutBtn').is_displayed())

def checkout_confirm():
    btn_confirm = browser.find_element_by_class_name('signOutBtn')
    btn_confirm.click()
    WebDriverWait(browser, 3).until(
        lambda x: x.find_element_by_class_name('fullscreenmask').is_displayed())

def open_driver():
    global browser
    #browser = webdriver.PhantomJS()
    #browser.set_window_size(1024, 768)
    chrome_options = Options()
    # 无头模式启动
    chrome_options.add_argument('--headless')
    # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--disable-gpu')
    # 初始化实例
    browser = webdriver.Chrome(chrome_options=chrome_options)

def run():
    login(USER, PASSWD)
    browser.get(INDEX_URL)
    checkout()
    checkout_confirm()


def main():
    open_driver()
    try:
        run()
    except Exception as err:
        print("err: " + str(err))

    browser.quit()

if __name__ == '__main__':
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    main()
