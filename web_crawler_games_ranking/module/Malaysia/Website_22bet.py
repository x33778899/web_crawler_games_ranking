import os

import module.Common_use as common_use
from module.Abstract_function.AbstractWebsite_ByClass import AbstractWebsite_ByClass


class Website_22bet(AbstractWebsite_ByClass):

    def __init__(self):
        super().__init__()

    @classmethod
    def reptile(cls):
        #  1.設定寫入目錄
        file_path = os.path.abspath(__file__)
        #  2.獲取該class 資料夾名稱
        save_path = common_use.storage_path(file_path)
        super().reptile_by_class(save_path + "/22bet", 'xgames-item__text',
                                 "https://22bet.com/tw/allgamesentrance"
                                 "?category=slot")
