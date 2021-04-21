import time
import os
import re
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
A="http://www.pbc.gov.cn/rmyh/index.html"
B = "https://poc.joysfintech.com/joys/login/pc_index.html?from=https%3A%2F%2Fpoc.joysfintech.com%2Fjoys%2Fpc_index.html%23%2F#/"
windows = driver.window_handles
driver.switch_to.window(windows[0])
driver.get(A)
driver.implicitly_wait(30)
driver.maximize_window()
try:
    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/a").click()   #点击货币政策按钮
except NoSuchElementException:
    print("未获取到货币政策按钮元素")
try:
    driver.find_element_by_xpath("/html/body/div[4]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/div/div/div[2]/table[6]/tbody/tr[4]/td/a").click() #点击利率政策
except NoSuchElementException:
    print("未获取到利率政策按钮元素")
handles = driver.window_handles
print("所有窗口句柄:", handles)   #打印所有句柄
driver.switch_to.window(handles[1])    #切换第二个句柄
try:
    driver.find_element_by_xpath("/html/body/div[4]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/div/table[6]/tbody/tr[2]/td[2]/table[2]").click()
except NoSuchElementException:
    print(("未定位到最新的LPR元素"))
    quit()
time.sleep(5)
handles1 = driver.window_handles
print("所有窗口句柄:", handles1)
driver.switch_to.window(handles1[2])
print("当前标题：",driver.title)
print("当前URL：",driver.current_url)
value = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[1]/td/div").text
print("当前的LPR信息：",value)
b  = value[22:26]
match = re.search('2021年(.+)月', value)
result2 = match.group(1)
match = re.search('月(.+)日', value)
result3 = match.group(1)
updatetime = b + "-" + result2 + "-" + result3
match = re.search('LPR为(\S+)%，', value)
result = match.group(1)
print (("1年期LPR为:{}%".format(result)))
match = re.search('5年期以上LPR为(.+)%。以上', value)
result1 = match.group(1)
print (("5年期LPR为:{}%".format(result1)))
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.get(B)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[2]/div[2]/input").send_keys("lsr")
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[2]/div[3]/input").send_keys("087686")
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[2]/div[5]").click()
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
a = driver.find_element_by_xpath('//*[text()="参数管理"]')
ActionChains(driver).move_to_element(a).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
b = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(b)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div/button[3]").click()   #点击新增按钮
els = driver.find_elements_by_class_name("el-input__inner")
els[0].click() #点击利率种类
time.sleep(3)
driver.find_element_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > div > li:nth-child(2)").click()  #点击LPR
els[3].send_keys(updatetime)
els[3]. send_keys(Keys.ENTER)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/form/div[2]/button[2]").click()   #点击保存按钮
driver.get_screenshot_as_file("D:/python/LPR/emails/test.jpg")
try:
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[2]/div[1]/div[1]/form/div/div[2]/div/div/div/input").send_keys(result)   #输入1年期
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[2]/div[1]/div[2]/form/div/div[2]/div/div/div/input").send_keys(result1)   #输入5年期
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[2]/div[1]/div[3]/button[2]").click()   #点击保存按钮
    time.sleep(2)
    driver.get_screenshot_as_file("D:/python/LPR/emails/test.jpg")
except NoSuchElementException:
    print("有执行中的单据")
time.sleep(2)
#driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/button").click() #点击提交按钮

driver.quit()