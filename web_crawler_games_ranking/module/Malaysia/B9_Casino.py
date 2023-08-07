import os

from selenium.webdriver.common.by import By

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByClass import AbstractWebsite_ByClass


class B9_Casino(AbstractWebsite_ByClass):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        cls._website_crawler(save_path + "/B9_Casino", "jm-item-title-asia",
                             "https://www.b9casinomyr.com/slot-royal.html")

    @classmethod
    def _website_crawler(cls, name, attributes, url):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 4. 抓取檔案
        data_find = wd.find_elements(By.CLASS_NAME, attributes)

        # 5. 按按鈕
        common_use.press_the_button(wd, By.XPATH,
                                    "//*[@id='lm_royal_top_close']/button")

        # 6. 寫入檔案
        cls._write_data(data_find, file_name, url)

    @classmethod
    def _write_data(cls, data, file_name, url):

        array = []
        count = 0

        for element in data:
            print(element.get_attribute("textContent"))
            count += 1
            if count > 19:
                break
            else:
                array.append(element.get_attribute("textContent"))

        common_use.write_data(array, file_name, url)
