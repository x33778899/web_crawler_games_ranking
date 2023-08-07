import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByXPath import AbstractWebsite_ByXPath


class White_Lion(AbstractWebsite_ByXPath):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        super().reptile_by_xpath_one_tab(save_path + "/White_Lion",
                                         '//*[@id="CategoryGames"]/div[',
                                         ']/a[1]/img',
                                         1,
                                         120,
                                         "https://www.whitelionplay.com/games/featuredGames",
                                         "//*[@id='CategoryGamesMenu']/nav/a[1]",
                                         "alt")

