import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class Megaslot(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        cls._website_crawler(save_path + "/Megaslot",
                             '/html/body/div[4]/div[2]/div/ui-view/div[2]/div/div/div/div/div/div[',
                             ']/div/div/div[2]/div[2]',
                             1,
                             120,
                             "https://www.megaslot.com/games/top")

    @classmethod
    def _website_crawler(cls, name, path_header, path_tail, start, end, url):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 4. 視窗拉到最下面
        scroll_element = wd.find_element(By.TAG_NAME, 'html')
        scroll_element.send_keys(Keys.END)  # 應為有用到響應式模擬滑鼠拖曳

        # 5. 計算網頁排名陣列
        web_rank_string_array = common_use.calculateWebRankDataByXPathElements(wd, start, end, path_header,
                                                                               path_tail)

        # 6. 寫檔
        common_use.write_data(web_rank_string_array, file_name, url)
