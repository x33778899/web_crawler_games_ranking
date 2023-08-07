import os

from selenium.webdriver.common.by import By

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class Wazamba(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        cls._website_crawler(save_path + "/Wazamba",
                             '/html/body/ui-view/ui-view/linda-app/ui-view/linda-view-layer-one/ui-view/'
                             'linda-view-layer-two/div/div[1]/ui-view/linda-casino-section/div[3]/div/div/'
                             'batman-search1/div/div[2]/div[3]/div[2]/div[1]/linda-game-item[',
                             ']/div/div[5]',
                             1,
                             30,
                             "https://wazamba.com/en/live-casino/top-rated",
                             "linda-toggle-favourite")

    @classmethod
    def _website_crawler(cls, name, path_header, path_tail, start, end, url, target="textContent"):
        # 1. 建立網頁驅動
        wd = common_use.createWd(url)

        # 2. 網頁睡眠
        common_use.web_sleep()

        # 3. 特殊處理
        search_input = wd.find_element(By.ID, "main-search")
        search_input.send_keys("slot")

        # 4. 計算檔名
        file_name = common_use.calculateFileName(name)

        # 5. 計算網頁排名陣列
        web_rank_string_array = common_use.calculateWebRankDataByXPathElements(wd, start, end, path_header,
                                                                               path_tail, target)

        # 6. 寫檔
        common_use.write_data(web_rank_string_array, file_name, url)
