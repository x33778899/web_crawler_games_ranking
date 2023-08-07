import os
import time

from selenium.webdriver.common.by import By

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class ME88(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        dictionary_file_name = {
            "/ME88_nextSpin": "https://www.me88play.asia/en-sg/slots/nextSpin",
            "/ME88_spadeGaming": "https://www.me88play.asia/en-sg/slots/spadeGaming",
            "/ME88_jili": "https://www.me88play.asia/en-sg/slots/jili",
            "/ME88_netent": "https://www.me88play.asia/en-sg/slots/netent",
            "/ME88_redtiger": "https://www.me88play.asia/en-sg/slots/redtiger",
            "/ME88_playNGo": "https://www.me88play.asia/en-sg/slots/playNGo"
        }
        for file_name, url in dictionary_file_name.items():
            cls._website_crawler(save_path + file_name,
                                 '//*[@id="root"]/div/div[2]/div[4]/div[2]/div/div/div/div[2]/ul/li[',
                                 ']/p/span',
                                 1,
                                 30,
                                 url)

    @classmethod
    def _website_crawler(cls, name, path_header, path_tail, start, end, url):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 4. 按按鈕
        common_use.press_the_button(wd, By.XPATH,
                                    "//*[@id='root']/div/div[2]/div[3]/div[2]/div/div/div/div[1]/ul/li[2]")

        time.sleep(2)
        # 4. 按按鈕

        common_use.press_the_button(wd, By.XPATH,
                                    "//*[@id='root']/div/div[2]/div[4]/div[2]/div/div/div/div[1]/ul/li[2]")

        common_use.press_the_button(wd, By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div[2]/div/div/div/div[2]/div")

        # 5. 計算網頁排名陣列
        web_rank_string_array = common_use.calculateWebRankDataByXPathElements(wd, start, end,
                                                                               path_header,
                                                                               path_tail
                                                                               )

        # 6. 寫檔
        common_use.write_data(web_rank_string_array, file_name, url)
