import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class Website_20_Bet(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        super().reptile_by_xpath_one_tab(save_path + "/20_Bet",
                                         '//*[@id="platform"]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div['
                                         '3]/div[',
                                         ']/div[2]/div/strong',
                                         1,
                                         50,
                                         "https://20bet.com/casino/hot",
                                         "//*[@id='platform']/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/"
                                         "div[3]/div[26]/div/div/button")

