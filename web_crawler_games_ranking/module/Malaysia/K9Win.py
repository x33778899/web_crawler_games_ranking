import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


# 相同網頁不同位置
class K9Win(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        super().reptile_by_xpath_one_tab(save_path + "/K9Win_pragmaticPlay",
                                         '/html/body/div[4]/div/div/div[2]/div[7]/div/div[2]/div[''1]/div/div[',
                                         ']/div/div[3]/p',
                                         1,
                                         50,
                                         "https://safebettingmy.k9win5.com/my/Home/CasinoGamesSlotsOnline",
                                         "/html/body/div[4]/div/div/div[1]/div[2]")

        super().reptile_by_xpath_one_tab(save_path + "/K9Win_joker",
                                         '/html/body/div[4]/div/div/div[2]/div[2]/div/div[2]/div[''1]/div/div[',
                                         ']/div/div[3]/p',
                                         1,
                                         50,
                                         "https://safebettingmy.k9win5.com/my/Home/CasinoGamesSlotsOnline",
                                         "/html/body/div[4]/div/div/div[1]/div[4]")

