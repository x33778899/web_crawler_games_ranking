import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByTagName import AbstractWebsite_ByTagName


class Lucky_Block(AbstractWebsite_ByTagName):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)

        super().reptile_by_tag(save_path + "/Lucky_Block",
                               "img",
                               "https://www.luckyblock.com/en/casino/category/lucky-block-picks",
                               "alt")

