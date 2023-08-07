import csv
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# 建立網頁驅動
def createWd(url):
    wd = webdriver.Chrome('./chromedriver')
    wd.implicitly_wait(10)
    try:
        wd.get(url)
    except:
        print("有時候網頁開不起來發生意外顯示出問題的網址:\n" + str(url))
    wd.maximize_window()  # 有幾個有做響應會因為視窗大小決定抓到幾個

    return wd


# 網頁睡眠
def web_sleep():
    time.sleep(5)


# 計算檔名
def calculateFileName(name):
    file_name = name + str(".csv")
    return file_name


# 用By.CLASS_NAME 抓取元素的擴充功能
# 1.選擇的抓取方式
# 2.網頁資料
# 3.是否尋找該元素裡的其他目標
def calculateWebRankDataByClassNameElements(attributes, wd, target="textContent"):
    result = []
    try:
        # 1. 抓取網頁元素
        elements = wd.find_elements(By.CLASS_NAME, attributes)

        # 2. 存放網頁元素字串
        for element in elements:
            element_target = element.get_attribute(target)
            if element_target != "":
                result.append(element_target)
            else:
                continue
    except:
        print("資料抓取失敗")
    return result


# 用By.Tag_name 抓取元素的擴充功能
# 1.選擇的抓取方式
# 2.網頁資料
# 3.是否尋找該元素裡的其他目標
def calculateWebRankDataByTagNameElements(attributes, wd, target="textContent"):
    result = []

    # 1. 抓取網頁元素
    try:
        elements = wd.find_elements(By.TAG_NAME, attributes)

        # 2. 存放網頁元素字串
        for element in elements:
            element_target = element.get_attribute(target)
            if element_target != "":
                result.append(element_target)
            else:
                continue
    except:
        print("資料抓取失敗")
    return result


# 用By.XPath 抓取元素的擴充功能
# 1.網頁資料
# 2.迴圈開始
# 3.迴圈結束
# 4.path 頭
# 5.path 尾
# 6.是否尋找該元素裡的其他目標
def calculateWebRankDataByXPathElements(wd, start, end, path_header, path_tail, target="textContent"):
    result = []
    try:
        for x in range(start, end):
            element = wd.find_element(By.XPATH,
                                      path_header +
                                      str(x) +
                                      path_tail)
            element_target = element.get_attribute(target)
            if element_target != "":
                result.append(element_target)
            else:
                continue
    except NoSuchElementException as e:
        print("使用定位模式抓取無法確定每次hot遊戲有幾個")
    except:
        print("資料抓取失敗")
    return result


def write_data(string_array, file_name, url):
    clear_file(file_name)
    for string in string_array:
        print(string)
        create_file(file_name, [string.strip(), url])


# 寫入檔案
def create_file(filename, head):
    with open(filename, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(head)
        csvfile.close()


# 清除檔案
def clear_file(filename):
    with open(filename, 'w') as file:
        file.write("")


# 模仿人工按按鈕
def press_the_button(wd, Method_of_obtaining, attributes):
    try:
        time.sleep(2)  # 按按鈕前停一下
        search_input = wd.find_element(Method_of_obtaining, attributes)
        search_input.click()
    except:
        print("沒有保護窗")


# 儲存路徑邏輯
def storage_path(file_path):
    # 获取当前脚本文件所在的目录路径

    dir_path = os.path.dirname(file_path)

    # 获取当前脚本文件所在的目录名
    dir_name = os.path.basename(dir_path)

    return "./Website_ranking/" + dir_name
