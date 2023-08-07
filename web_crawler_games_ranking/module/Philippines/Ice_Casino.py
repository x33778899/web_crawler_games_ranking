import os

from selenium.webdriver.common.by import By

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByClass import AbstractWebsite_ByClass


class Ice_Casino(AbstractWebsite_ByClass):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        cls._website_crawler(save_path + "/Ice_Casino", 'tmb-lobby__title',
                             "https://icecasino.com/en/popular")

    @classmethod
    def _website_crawler(cls, name, attributes, url):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 4. 計算網頁排名陣列
        web_rank_string_array = common_use.calculateWebRankDataByClassNameElements(attributes, wd)

        # 5. 按鈕有保護框
        common_use.press_the_button(wd, By.CLASS_NAME, "i-close")

        # 6. 寫檔
        common_use.write_data(web_rank_string_array, file_name, url)


